from pico2d import *
import random


WIDTH, HEIGHT = 800, 600
open_canvas(WIDTH, HEIGHT)

kpu_ground=load_image('Resource\Hospital1.png')
class Hero:
    def __init__(self ):
        self.x,self.y=0,0
        self.frame=0
        self.walk_mode=0   #0=idle 1= up 2= down 3= Lup 4= Left 5= Ldown 6=Rup 7=Right 8=Rdown
        self.idle=load_image('Resource\hero\idle.png')
        self.move=load_image('Resource\hero\Walk.png')
    def update(self):
        if(self.walk_mode<=8):
            self.frame=(self.frame+1)%6
    def draw(self):
        if (self.walk_mode == 0):
            self.idle.clip_draw(self.frame*32,0,32,100,self.x,self.y)
        elif (self.walk_mode == 1):
            self.move.clip_draw(self.frame*33,630,33,100,self.x,self.y)
        elif (self.walk_mode == 2):
            self.move.clip_draw(self.frame * 33, 730, 33, 100, self.x, self.y)
        elif (self.walk_mode == 3):
            self.move.clip_draw(self.frame * 42, 320, 42, 100, self.x, self.y)
        elif (self.walk_mode == 4):
            self.move.clip_draw(self.frame * 51, 420, 51, 100, self.x, self.y)
        elif (self.walk_mode == 5):
            self.move.clip_draw(self.frame * 43, 520, 43, 100, self.x, self.y)
        elif (self.walk_mode == 6):
            self.move.clip_draw(self.frame * 42, 0, 42, 100, self.x, self.y)
        elif (self.walk_mode == 7):
            self.move.clip_draw(self.frame * 51, 110, 51, 100, self.x, self.y)
        elif (self.walk_mode == 8):
            self.move.clip_draw(self.frame * 43, 210, 43, 100, self.x, self.y)

class NPC:
    def __init__(self):
        self.x,self.y=0,0
        self.direct=0 #0=up 1= down 2= left 3= right
        self.form=random.randint(0, 8)
        if( self.form==0):
            self.image=load_image('Resource\\NPC\Girl1.png')
        elif ( self.form== 1):
            self.image = load_image('Resource\\NPC\Girl2.png')
        elif ( self.form == 2):
            self.image = load_image('Resource\\NPC\Girl3.png')
        elif ( self.form == 3):
            self.image = load_image('Resource\\NPC\Girl4.png')
        elif ( self.form == 4):
            self.image = load_image('Resource\\NPC\Girl5.png')
        elif ( self.form == 5):
            self.image = load_image('Resource\\NPC\Man1.png')
        elif ( self.form == 6):
            self.image = load_image('Resource\\NPC\Man2.png')
        elif ( self.form == 7):
            self.image = load_image('Resource\\NPC\Man3.png')
        elif ( self.form == 8):
            self.image = load_image('Resource\\NPC\Man4.png')

    def draw(self):
        if (self.direct == 0):
            self.image.clip_draw(self.direct*32,0,32,100,self.x,self.y)
        elif (self.direct == 1):
            self.image.clip_draw(self.direct*32,0,33,100,self.x,self.y)
        elif (self.direct == 2):
            self.image.clip_draw(self.direct * 32, 0, 33, 100, self.x, self.y)
        elif (self.direct == 3):
            self.image.clip_draw(self.direct * 32, 0, 42, 100, self.x, self.y)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()

def draw_line(p1, p2):
    while True:
        hero=Hero()
        npc=NPC()
        frame = 0
        hero.walk_mode=8
        for i in range(0,100+1,2):
            clear_canvas()
            kpu_ground.draw(WIDTH // 2, HEIGHT // 2)

            t= i /100
            hero.x = (1 - t) * p1[0] + t * p2[0]
            hero.y = (1 - t) * p1[1] + t * p2[1]
            npc.x=100
            npc.y=300
            hero.draw()
            npc.draw()
            update_canvas()
            hero.update()
            delay(0.1)
            handle_events()
    pass


size = 20
points=[(random.randint(100,700),random.randint(100,500))for i in range(size)]
n=1

while True:
    draw_line(points[n-1], points[n])
    n=(n+1)%size
    get_events()

