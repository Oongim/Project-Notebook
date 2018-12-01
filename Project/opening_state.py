import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image,textbox,text,font,text_cnt,text_sequence,image_sequence,fonts,bgm
    image = [load_image('Resource\opening\clock.png'),
             load_image('Resource\opening\People1.png'),
             load_image('Resource\opening\opening3.png'),
             load_image('Resource\opening\\manual.png')
             ]
    textbox=load_image('Resource\\UI\\textbox.png')
    text=['현재 시각 11:30분 ',
          '유일하게 밥을 먹을 수 있는 공강시간',
          '사람이 가장 많은 시간이지만 오늘은 유난히 많은 것 같다.',
          '다음 수업 시간에 늦으면 "F", 절대 늦으면 안된다.',
          '사람들 빈 곳으로 200명만 추월 한다면 가능 할 것 같다. ',
          ''
          ]
    font = load_font('서울남산 장체B.ttf', 30)
    fonts = load_font('서울남산 장체B.ttf', 20)
    text_cnt=0
    text_sequence=0
    image_sequence=0
    bgm = load_music('Resource\\Music\\opening_bgm.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
def exit():
    global image,textbox,font,fonts,bgm
    del(image)
    del(textbox)
    del(font)
    del(fonts)
    del(bgm)
def handle_events():
   global image_sequence
   events=get_events()
   for event in events:
       if event.type == SDL_QUIT:
           game_framework.quit()
       else:
           if(event.type, event.key)==(SDL_KEYDOWN, SDLK_ESCAPE):
               game_framework.quit()
           elif(event.type, event.key)==(SDL_KEYDOWN, SDLK_SPACE):
               if(image_sequence==3):
                   game_framework.change_state(main_state)
               else:
                   image_sequence = 3

def draw():
    clear_canvas()

    if (image_sequence != 3):
        image[image_sequence].clip_draw(0, 0, 800, 500, 400, 350)
        textbox.clip_draw(0, 0, 800, 600, 400, 300)
        font.draw(50, 90, text[text_sequence][:text_cnt], (255, 255, 0))
        fonts.draw(680, 20, 'skip "space"', (100, 100, 100))
    else:
        image[image_sequence].clip_draw(0, 0, 800, 598, 400, 300)
    update_canvas()
    delay(0.1)

def update():
    global text_cnt,text_sequence,image_sequence

    text_cnt=(text_cnt+1)
    if(text_cnt>=len(text[text_sequence])+1):
        if(image_sequence != 3):
            text_sequence+=1
            text_cnt=0
            delay(1)
            if(text_sequence==2):
                image_sequence+=1
            elif (text_sequence == 3):
                image_sequence += 1
            elif (text_sequence == 5):
                image_sequence += 1
def pause():
    pass


def resume():
    pass






