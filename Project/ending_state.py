import game_framework
import title_state
import main_state
import random

from pico2d import *

class Judge:
    sprite_position = [[82, 140], [82, 140], [82, 140], [98, 140], [98, 140], [84, 0]]
    def __init__(self):
        self.image = [load_image('Resource\ending\\0.png'),
                 load_image('Resource\ending\\1.png'),
                 load_image('Resource\ending\\2.png'),
                 load_image('Resource\ending\\3.png'),
                 load_image('Resource\ending\\4.png')]
        self.frame = random.randint(0, 3)
        self.x=0
        self.y=480
    def draw(self):
        self.image[self.frame].clip_draw(0,0,Judge.sprite_position[self.frame][0], Judge.sprite_position[self.frame][1], self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 5
def enter():
    global judge,frame,back,font
    font = load_font('서울남산 장체B.ttf', 16)
    back=load_image('Resource\ending\Counter.png')
    judge = [Judge() for i in range(4)]
    for i in range(4):
        judge[i].x=260+98*i
def exit():
    global judge,back,font
    del (judge)
    del(back)
    del(font)
    del(main_state.cnt)
def update():
    global frame
    for i in range(4):
        judge[i].update()

def draw():
    clear_canvas()
    back.draw_now(400, 200)
    for i in range(4):
        judge[i].draw()
    update_canvas()
    delay(0.1)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type) == (SDL_KEYDOWN):
                game_framework.change_state(title_state)

def pause(): pass

def resume(): pass
