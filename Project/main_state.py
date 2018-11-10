from pico2d import *
import random
import game_framework
import title_state

from Hero import Hero
from NPC import NPC
from Map import Map

class Count:
    def __init__(self):
        self.x=730
        self.y=560
        self.count=0
        self.number=[load_image('Resource\Count\\0.png'),
                     load_image('Resource\Count\\1.png'),
                     load_image('Resource\Count\\2.png'),
                     load_image('Resource\Count\\3.png'),
                     load_image('Resource\Count\\4.png'),
                     load_image('Resource\Count\\5.png'),
                     load_image('Resource\Count\\6.png'),
                     load_image('Resource\Count\\7.png'),
                     load_image('Resource\Count\\8.png'),
                     load_image('Resource\Count\\9.png')]
    def update(self):
        self.y -= 100
        self.count+=1
        if self.y <= 0:
            self.y += 600
    def draw(self):
        count=self.count
        posx=self.x
        while(count!=0):
            self.number[count % 10].clip_draw(0, 0, 13, 30, posx, self.y,10,24)
            count=count//10;
            posx-=10
def make_NPCblank_Init():
    rand_num = 2
    npc[0][rand_num].direct = 5

    for i in range(1, 7):
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

    for i in range(6,-1,-1):
        for j in range(0,4):
            npc[i][j].x=100*j+250
            npc[i][j].y=100*i+100


def draw_NPC():
    for i in range(6,-1,-1):
        for j in range(0,4):
            npc[i][j].draw()


def choice_Change_NPC(rand_num):
    if rand_num == 0:
        rand_num = 1
        npc[6][rand_num].direct = 6
        npc[6][rand_num].x -= 100
    elif rand_num == 1:
        rand_num = random.randint(0, 2)
        if npc[6][rand_num].direct != 5:
            npc[6][rand_num].direct = 6  # Change
            if rand_num==0:
                npc[6][rand_num].x+=100
            elif rand_num==2:
                npc[6][rand_num].x -= 100
    elif rand_num == 2:
        rand_num = random.randint(1, 3)
        if npc[6][rand_num].direct != 5:
            npc[6][rand_num].direct = 6  # Change
            if rand_num==1:
                npc[6][rand_num].x+=100
            elif rand_num==3:
                npc[6][rand_num].x -= 100
    elif rand_num == 3:
        rand_num = 2
        npc[6][rand_num].direct = 6
        npc[6][rand_num].x += 100


def make_NPC_New(rand_num):
    for i in range(0, 4):
        npc[6][i].form = random.randint(0, 8)
        npc[6][i].direct = 0
    if rand_num == 0:
        rand_num = random.randint(0, 1)
        npc[6][rand_num].direct = 5  # Blank Position
    elif rand_num == 1:
        rand_num = random.randint(0, 2)
        npc[6][rand_num].direct = 5  # Blank
    elif rand_num == 2:
        rand_num = random.randint(1, 3)
        npc[6][rand_num].direct = 5  # Blank Position
    elif rand_num == 3:
        rand_num = random.randint(2, 3)
        npc[6][rand_num].direct = 5  # Blank Position
    if(cnt.count>=25):
        if ((cnt.count ) % 5==0):
            choice_Change_NPC(rand_num)



def move_NPC():
    cnt.update()
    for i in range(6,-1,-1):  #move NPC y Position
        for j in range(0,4):
            npc[i][j].y-=100
            if npc[i][j].y==-100:
                npc[i][j].y=600
            if (npc[i][j].direct == 6):
                if (npc[i][j - 1].direct == 5):
                    npc[i][j].change(j, j - 1, i)
                elif (npc[i][j + 1].direct == 5):
                    npc[i][j].change(j, j + 1, i)
    for i in range(1,7):      #move NPC list position
        npc[i-1], npc[i]=npc[i],npc[i-1]
    if (npc[5][0].direct==5):
        make_NPC_New(0)
    elif (npc[5][1].direct==5):
        make_NPC_New(1)
    elif (npc[5][2].direct==5):
        make_NPC_New(2)
    elif (npc[5][3].direct==5):
        make_NPC_New(3)




def enter():
    global hero,npc,end,map,cnt
    map=Map()
    cnt=Count()
    end=False
    hero = Hero()
    npc = [[NPC() for i in range(4)] for i in range(7)]
    make_NPCblank_Init()  # 빈칸 생성

def exit():
    global hero, npc
    del(hero)
    del(npc)


def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            hero.handle_event(event)

def update():
    hero.update()


def draw():
    clear_canvas()
    #################################
    map.draw()
    draw_NPC()
    hero.draw()
    cnt.draw()
    #################################
    update_canvas()
    delay(0.1)
