from pico2d import *
import main_state
import game_framework
import death_state

import random

RIGHT_DOWN,LEFT_DOWN,UP_DOWN,DEATH,IDLE =range(5)
#0=idle 1= up 2= down 3= Lup 4= Left 5= Ldown 6=Rup 7=Right 8=Rdown
UP_DIRECTION,LEFT_DIRECTION,RIGHT_DIRECTION=range(3)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_DOWN,
}

class IdleState:
    @staticmethod
    def enter(Hero,event):
        Hero.frame = 0

    @staticmethod
    def exit(Hero,event):
        pass

    @staticmethod
    def do(Hero):
        Hero.frame = (Hero.frame + 1) % 11

    @staticmethod
    def draw(Hero):
        Hero.idle.clip_draw((Hero.frame//2) * 64, 0, 64, 200, Hero.x, Hero.y)

PIXEL_PER_METER = (10.0/0.2)
RUN_SPEED_KMPH = 33.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0/TIME_PER_ACTION
FRAMES_PER_ACTION = 6
TIME_PER_MOVE=100
class RunState:
    @staticmethod
    def enter(Hero, event):
        Hero.frame = 0
        if event == RIGHT_DOWN:
            Hero.position =  min(3,Hero.position+1)
            Hero.velocity=1
        elif event == LEFT_DOWN:
            Hero.position =  max(0,Hero.position-1)
            Hero.velocity = -1
        elif event == UP_DOWN:
            Hero.velocity = 0

    @staticmethod
    def exit(Hero, event):
        Hero.frame = 0
        Hero.x=100*Hero.position+250
        main_state.change_NPC_column()
        main_state.map.normalize_position()
        main_state.cnt.plus_count()
        if Hero.Collosion()==1:
            Hero.frame = 0
            Hero.add_event(DEATH)
    @staticmethod
    def do(Hero):
        Hero.frame = int((Hero.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time))% 7

        Hero.x += Hero.velocity*RUN_SPEED_PPS*game_framework.frame_time
        main_state.move_NPC(RUN_SPEED_PPS*game_framework.frame_time)
        main_state.map.update(RUN_SPEED_PPS*game_framework.frame_time)
        main_state.cnt.update(main_state.map.y[0])
        if (Hero.frame == 6):
            Hero.add_event(IDLE)
    sprite_position=[[66,1250],[66,1460],[84,640],[102,840],[86,1040],[84,0],[102,220],[86,420]]
    @staticmethod
    def draw(hero):
            hero.move.clip_draw(hero.frame*RunState.sprite_position[hero.walk_mode][0],RunState.sprite_position[hero.walk_mode][1]
                                ,RunState.sprite_position[hero.walk_mode][0],200,hero.x,hero.y)

class DeathState:
    @staticmethod
    def enter(hero,event):
        pass

    @staticmethod
    def exit(hero,event):
       pass

    @staticmethod
    def do(hero):
        hero.frame = (hero.frame + 1)
        hero.x+=10
        delay(0.1)
        if (hero.frame == 4):
            game_framework.change_state(death_state)

    @staticmethod
    def draw(hero):
        hero.bounce[hero.frame].clip_draw(0, 0, 81, 200, hero.x, hero.y)

next_state_table = {
    IdleState: {UP_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,DEATH: DeathState,
                DEATH: DeathState}
    ,RunState: {DEATH: DeathState,IDLE:IdleState,
                UP_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState},
    DeathState:{ UP_DOWN: DeathState, RIGHT_DOWN: DeathState, LEFT_DOWN: DeathState,
                 DEATH: DeathState}
        }
class Hero:
    def __init__(self ):
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.position = 2
        self.x,self.y=100 * self.position + 250,100
        self.frame=0
        self.velocity=0
        self.walk_mode=UP_DIRECTION
        self.idle=load_image('Resource\hero\idle.png')
        self.move=load_image('Resource\hero\Walk.png')
        self.bounce=[load_image('Resource\hero\Collosion\\1.png'),
                     load_image('Resource\hero\Collosion\\2.png'),
                     load_image('Resource\hero\Collosion\\3.png'),
                     load_image('Resource\hero\Collosion\\4.png')]



    def add_event(self, event):
         self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def Collosion(self):
        for i in range(0, 4):
            if main_state.EMPTY == main_state.npc[0][i].state:
                if (self.position != i):
                    return True