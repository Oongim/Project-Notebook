from pico2d import *
import main_state
import game_framework
import death_state

import random

RIGHT_DOWN,LEFT_DOWN,UP_DOWN,DEATH,IDLE =range(5)
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
        Hero.frame = (Hero.frame + 1) % 6

    @staticmethod
    def draw(Hero):
        Hero.idle.clip_draw(Hero.frame * 64, 0, 64, 200, Hero.x, Hero.y)

class RunState:
    @staticmethod
    def enter(Hero, event):
        Hero.frame = 0
        if event == RIGHT_DOWN:
            Hero.position += 1
            if Hero.position == 4:
                Hero.position = 3
            else:
                Hero.walk_mode = 1
                main_state.move_NPC()
                main_state.map.update()
        elif event == LEFT_DOWN:
            Hero.position -= 1
            if Hero.position == -1:
                Hero.position = 0
            else:
                Hero.walk_mode = 1
                main_state.move_NPC()
                main_state.map.update()
        elif event == UP_DOWN:
            Hero.walk_mode = 1
            main_state.move_NPC()
            main_state.map.update()

    @staticmethod
    def exit(Hero, event):
        Hero.frame = 0

    @staticmethod
    def do(Hero):
        Hero.frame = Hero.frame + 1
        Hero.x = 100 * Hero.position + 250
        if Hero.Collosion()==1:
            Hero.frame = 0
            Hero.add_event(DEATH)
        if (Hero.frame == 6):
            Hero.add_event(IDLE)

    @staticmethod
    def draw(hero):
        if (hero.walk_mode == 1):
            hero.move.clip_draw(hero.frame*66,1250,66,200,hero.x,hero.y)
        elif (hero.walk_mode == 2):
            hero.move.clip_draw(hero.frame * 66, 1460, 66, 200, hero.x, hero.y)
        elif (hero.walk_mode == 3):
            hero.move.clip_draw(hero.frame * 84, 640, 84, 200, hero.x, hero.y)
        elif (hero.walk_mode == 4):
            hero.move.clip_draw(hero.frame *102, 840, 102, 200, hero.x, hero.y)
        elif (hero.walk_mode == 5):
            hero.move.clip_draw(hero.frame * 86, 1040, 86, 200, hero.x, hero.y)
        elif (hero.walk_mode == 6):
            hero.move.clip_draw(hero.frame * 84, 0, 84, 200, hero.x, hero.y)
        elif (hero.walk_mode == 7):
            hero.move.clip_draw(hero.frame * 102, 220, 102, 200, hero.x, hero.y)
        elif (hero.walk_mode == 8):
            hero.move.clip_draw(hero.frame * 86, 420, 86, 200, hero.x, hero.y)

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
        if (hero.frame == 4):
            game_framework.change_state(death_state)

    @staticmethod
    def draw(hero):
        hero.bounce[hero.frame].draw_now(400, 300)

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

        self.walk_mode=0   #0=idle 1= up 2= down 3= Lup 4= Left 5= Ldown 6=Rup 7=Right 8=Rdown
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
            if 5 == main_state.npc[0][i].direct:
                if (self.position != i):
                    return True