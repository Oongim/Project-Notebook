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
        self.zero=load_image('Resource\Count\\0.png')
        self.one = load_image('Resource\Count\\1.png')
        self.two = load_image('Resource\Count\\2.png')
        self.three = load_image('Resource\Count\\3.png')
        self.four = load_image('Resource\Count\\4.png')
        self.five = load_image('Resource\Count\\5.png')
        self.six = load_image('Resource\Count\\6.png')
        self.seven = load_image('Resource\Count\\7.png')
        self.eight = load_image('Resource\Count\\8.png')
        self.nine = load_image('Resource\Count\\9.png')
    def update(self):
        self.y -= 100
        self.count+=1
        if self.y <= 0:
            self.y += 600
    def draw(self):
        count=self.count
        posx=self.x
        while(count!=0):
            if (count % 10 == 0):
                self.zero.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 1):
                self.one.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 2):
                self.two.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 3):
                self.three.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 4):
                self.four.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 5):
                self.five.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 6):
                self.six.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 7):
                self.seven.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 8):
                self.eight.clip_draw(0, 0, 13, 30, posx, self.y)
            elif (count % 10 == 9):
                self.nine.clip_draw(0, 0, 13, 30, posx, self.y)
            count=count//10;
            posx-=13
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
    cnt.update()
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

def Collosion():
    global end
    for i in range(0, 4):
        if 5==npc[0][i].direct:
            if(hero.position!=i):
                end=True


def enter():
    global hero,npc,end,map,cnt
    map=Map()
    cnt=Count()
    end=False
    hero = Hero()
    npc = [[NPC() for i in range(4)] for i in range(6)]
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

    if(end):
        game_framework.change_state(title_state)
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