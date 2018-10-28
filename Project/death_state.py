import game_framework
import title_state
from pico2d import *

def enter():
    global death,frame,back
    back=load_image('Resource\hero\Death\\death.png')
    death = [load_image('Resource\hero\Death\\1.png'),
                  load_image('Resource\hero\Death\\2.png'),
                  load_image('Resource\hero\Death\\3.png'),
                  load_image('Resource\hero\Death\\4.png'),
                  load_image('Resource\hero\Death\\5.png'),
                  load_image('Resource\hero\Death\\6.png'),
                  load_image('Resource\hero\Death\\7.png'),
                  load_image('Resource\hero\Death\\8.png'),
                  load_image('Resource\hero\Death\\9.png'),
                  load_image('Resource\hero\Death\\10.png'),
                  load_image('Resource\hero\Death\\11.png'),
                  load_image('Resource\hero\Death\\12.png'),
                  load_image('Resource\hero\Death\\13.png'),
                  load_image('Resource\hero\Death\\14.png'),
                  load_image('Resource\hero\Death\\15.png'),
                  load_image('Resource\hero\Death\\16.png'),
                  load_image('Resource\hero\Death\\17.png'),
                  load_image('Resource\hero\Death\\18.png'),
                  load_image('Resource\hero\Death\\19.png'),
                  load_image('Resource\hero\Death\\20.png')]
    frame=0

def exit():
    global death,back
    del (death)
    del(back)

def update():
    global frame
    if (frame < 19):
        frame = (frame + 1)



def draw():
    clear_canvas()
    back.draw_now(400, 300)
    death[frame].draw_now(400, 300)

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
