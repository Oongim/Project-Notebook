import game_framework
import opening_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image,hero,frame,name,press
    frame=0
    image = load_image('Resource\\title.png')
    hero=load_image('Resource\hero\\main.png')
    name=load_image('Resource\\HakSick.png')
    press=load_image('Resource\\Press.png')
def exit():
    global image,hero,name,press
    del(image)
    del(hero)
    del(name)
    del(press)

def handle_events():
   events=get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       else:
           if(event.type, event.key)==(SDL_KEYDOWN, SDLK_ESCAPE):
               game_framework.quit()
           elif(event.type)==(SDL_KEYDOWN):
               game_framework.change_state(opening_state)

def draw():
    clear_canvas()
    image.clip_draw(0, 0, 800, 600, 400, 300)
    name.clip_draw(0, 0, 380, 220, 400, 600-110)
    if(frame%4<2):
        press.clip_draw(0, 0, 284, 67, 400, 50)
    if(frame<5):
        hero.clip_draw(frame* 144, 0, 144, 300, 220, 220)
    else:
        hero.clip_draw((9-frame) * 144, 0, 144, 300, 220, 220)
    delay(0.3)
    update_canvas()







def update():
    global frame
    frame=(frame+1)%10



def pause():
    pass


def resume():
    pass






