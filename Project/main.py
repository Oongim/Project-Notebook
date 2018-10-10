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
        if(self.walk_mode==0):
            self.frame=(self.frame+1)%6
        elif(self.walk_mode<=8):
            self.frame = self.frame + 1
            if(self.frame==6):
                self.walk_mode = 0
                self.frame = 0
    def draw(self):
        if (self.walk_mode == 0):
            self.idle.clip_draw(self.frame*64,0,64,200,self.x,self.y)
        elif (self.walk_mode == 1):
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

    for i in range(5,-1,-1):
        for j in range(0,4):
            npc[i][j].x=100*j+250
            npc[i][j].y=100*i+100
def draw_NPC():
    for i in range(5,-1,-1):
        for j in range(0,4):
            npc[i][j].draw()

def make_NPC_New(rand_num):
    for i in range(0, 4):
        npc[5][i].form = random.randint(0, 8)
        npc[5][i].direct=0
    if rand_num == 0:
        rand_num = random.randint(0, 1)
        npc[5][rand_num].direct = 5  # Blank Position
    elif rand_num == 1:
        rand_num = random.randint(0, 2)
        npc[5][rand_num].direct = 5  # Blank
    elif rand_num == 2:
        rand_num = random.randint(1, 3)
        npc[5][rand_num].direct = 5  # Blank Position
    elif rand_num == 3:
        rand_num = random.randint(2, 3)
        npc[5][rand_num].direct = 5  # Blank Position
def move_NPC():
    for i in range(5,-1,-1):  #move NPC y Position
        for j in range(0,4):
            npc[i][j].y-=100
            if npc[i][j].y==0:
                npc[i][j].y=600
    for i in range(1,6):      #move NPC list position
        npc[i-1], npc[i]=npc[i],npc[i-1]
    if (npc[4][0].direct==5):
        make_NPC_New(0)
    elif (npc[4][1].direct==5):
        make_NPC_New(1)
    elif (npc[4][2].direct==5):
        make_NPC_New(2)
    elif (npc[4][3].direct==5):
        make_NPC_New(3)

def draw_hero():
    hero.x = 100 * hero.position + 250
    hero.y = 100
    hero.draw()
    hero.update()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                hero.position += 1
                if hero.position==4:
                    hero.position = 3
                else:
                    hero.walk_mode=1
                    move_NPC()
            elif event.key == SDLK_LEFT:
                hero.position -= 1
                if hero.position==-1:
                    hero.position = 0
                else:
                    hero.walk_mode = 1
                    move_NPC()
            elif event.key == SDLK_UP:
                hero.walk_mode = 1
                move_NPC()
            elif event.key == SDLK_ESCAPE:
                running = False



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
    delay(0.1)