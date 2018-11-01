import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image,textbox,text,font,text_cnt
    image = [load_image('Resource\opening\People1.png'),
             load_image('Resource\opening\People2.png')]
    textbox=load_image('Resource\\UI\\textbox.png')
    text='현재 시각 11:30분 공강이다.'
    font = load_font('서울남산 장체B.ttf', 30)
    text_cnt=0
def exit():
    global image,textbox
    del(image)
    del(textbox)

def handle_events():
   events=get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       else:
           if(event.type, event.key)==(SDL_KEYDOWN, SDLK_ESCAPE):
               game_framework.quit()
           elif(event.type)==(SDL_KEYDOWN):
               game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image[0].clip_draw(0, 0, 800, 550, 400, 400)
    textbox.clip_draw(0, 0, 800, 600, 400, 300)
    font.draw(50, 90, text[:text_cnt], (255, 255, 0))
    update_canvas()
    delay(0.1)

def update():
    global text_cnt
    text_cnt=(text_cnt+1)%(len(text)+1)

def pause():
    pass


def resume():
    pass






