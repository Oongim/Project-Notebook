from pico2d import *
import random


WIDTH, HEIGHT = 800, 600
open_canvas(WIDTH, HEIGHT)

kpu_ground=load_image('Resource\Hospital1.png')
class Hero:
    def __init__(self ):
        self.x,self.y=0,0
        self.frame=0
        self.position=2
        self.walk_mode=0   #0=idle 1= up 2= down 3= Lup 4= Left 5= Ldown 6=Rup 7=Right 8=Rdown
        self.idle=load_image('Resource\hero\idle.png')
        self.move=load_image('Resource\hero\Walk.png')
    def update(self):
        if(self.walk_mode<=8):
            self.frame=(self.frame+1)%6

    def draw(self):
        if (self.walk_mode == 0):
            self.idle.clip_draw(self.frame*64,0,64,200,self.x,self.y)
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
            self.image.clip_draw(self.direct*64,0,64,200,self.x,self.y)
        elif (self.direct == 1):
            self.image.clip_draw(self.direct*64,0,64,200,self.x,self.y)
        elif (self.direct == 2):
            self.image.clip_draw(self.direct * 64, 0, 64, 200, self.x, self.y)
        elif (self.direct == 3):
            self.image.clip_draw(self.direct * 64, 0, 64, 200, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
def make_NPCblank_Init():
    rand_num = 2
    npc[0][rand_num].direct = 5
    for i in range(1, 6):
        if rand_num == 0:
            rand_num = random.randint(0, 1)
            npc[i][rand_num].direct = 5  # Blank Position
        elif rand_num == 1:
            rand_num = random.randint(0, 2)
            npc[i][rand_num].direct = 5  # Blank
        elif rand_num == 2:
            rand_num = random.randint(1, 3)
            npc[i][rand_num].direct = 5  # Blank Position
        elif rand_num == 3:
            rand_num = random.randint(2, 3)
            npc[i][rand_num].direct = 5  # Blank Position
def draw_NPC():
    for i in range(5,-1,-1):
        for j in range(0,4):
            npc[i][j].x=100*j+250
            npc[i][j].y=100*i+100
            npc[i][j].draw()
def draw_hero():
    hero.x = 100 * hero.position + 250
    hero.y = 100
    hero.draw()
    hero.update()
#main
hero=Hero()
npc=[[NPC() for i in range(4)] for i in range(6)]

make_NPCblank_Init()  #빈칸 생성


running = True
while running:
    handle_events()
    clear_canvas()
    #################################

    draw_NPC()
    draw_hero()

    #################################
    update_canvas()
    get_events()
    delay(0.2)