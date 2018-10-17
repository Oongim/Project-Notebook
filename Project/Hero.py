from pico2d import *
import main_state
import random
IDLE,RUN=range(2)
RIGHT_DOWN,LEFT_DOWN,UP_DOWN =range(3)
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_DOWN,
}
next_state_table = {
    IDLE: {UP_DOWN:RUN ,RIGHT_DOWN:RUN,LEFT_DOWN: RUN},
    RUN: {UP_DOWN:IDLE,LEFT_DOWN:IDLE,RIGHT_DOWN:IDLE}
}

class Hero:
    def __init__(self ):
        self.event_que = []
        self.cur_state = IDLE
        self.position = 2
        self.x,self.y=100 * self.position + 250,100
        self.frame=0

        self.walk_mode=0   #0=idle 1= up 2= down 3= Lup 4= Left 5= Ldown 6=Rup 7=Right 8=Rdown
        self.idle=load_image('Resource\hero\idle.png')
        self.move=load_image('Resource\hero\Walk.png')

    def enter_IDLE(self):
        self.frame = 0

    def exit_IDLE(self):
        pass
    def do_IDLE(self):
        self.frame = (self.frame + 1) % 6

    def draw_IDLE(self):
        self.idle.clip_draw(self.frame * 64, 0, 64, 200, self.x, self.y)

    def enter_RUN(self):
        self.frame = 0

    def exit_RUN(self):
        pass
    def do_RUN(self):
        self.frame = self.frame + 1
        self.x = 100 * self.position + 250
        if (self.frame == 6):
            self.cur_state=IDLE
            self.update()
    def draw_RUN(self):
        if (self.walk_mode == 1):
            self.move.clip_draw(self.frame*66,1250,66,200,self.x,self.y)
        elif (self.walk_mode == 2):
            self.move.clip_draw(self.frame * 66, 1460, 66, 200, self.x, self.y)
        elif (self.walk_mode == 3):
            self.move.clip_draw(self.frame * 84, 640, 84, 200, self.x, self.y)
        elif (self.walk_mode == 4):
            self.move.clip_draw(self.frame *102, 840, 102, 200, self.x, self.y)
        elif (self.walk_mode == 5):
            self.move.clip_draw(self.frame * 86, 1040, 86, 200, self.x, self.y)
        elif (self.walk_mode == 6):
            self.move.clip_draw(self.frame * 84, 0, 84, 200, self.x, self.y)
        elif (self.walk_mode == 7):
            self.move.clip_draw(self.frame * 102, 220, 102, 200, self.x, self.y)
        elif (self.walk_mode == 8):
            self.move.clip_draw(self.frame * 86, 420, 86, 200, self.x, self.y)

    def add_event(self, event):
         self.event_que.insert(0, event)
    def change_state(self,  state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state
    enter_state = {IDLE:enter_IDLE,RUN:enter_RUN}
    exit_state = {IDLE: exit_IDLE, RUN: exit_RUN}
    do_state = {IDLE: do_IDLE, RUN: do_RUN}
    draw_state = {IDLE: draw_IDLE, RUN: draw_RUN}

    def update(self):
        self.do_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
        self.draw_state[self.cur_state](self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.position += 1
                if self.position == 4:
                    self.position = 3
                else:
                    self.walk_mode = 1
                    main_state.move_NPC()
                    main_state.Collosion()
            elif key_event == LEFT_DOWN:
                self.position -= 1
                if self.position == -1:
                    self.position = 0
                else:
                    self.walk_mode = 1
                    main_state.move_NPC()
                    main_state.Collosion()
            elif key_event == UP_DOWN:
                self.walk_mode = 1
                main_state.move_NPC()
                main_state.Collosion()
            self.add_event(key_event)
