from pico2d import *
import random


KPU_WIDTH, KPU_HEIGHT = 800, 600
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('Resource\hospital1.png')
character = load_image('Resource\walk\walk.png')

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()

def draw_line(p1, p2):

    frame = 0
    for i in range(0,100+1,2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        t= i /100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]

        if p1<p2:
            character.clip_draw(frame * 32, 0, 32, 100, x, y)
        elif p1>p2:
            character.clip_draw(frame * 32, 0, 32, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 6
        delay(0.5)
        handle_events()
    pass


size = 20
points=[(random.randint(100,700),random.randint(100,500))for i in range(size)]
n=1

while True:
    draw_line(points[n-1], points[n])
    n=(n+1)%size
    get_events()

