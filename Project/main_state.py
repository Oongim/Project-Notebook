from pico2d import *
import random
import game_framework
import title_state

from Hero import Hero
from NPC import NPC



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

def Collosion():
    global end
    for i in range(0, 4):
        if 5==npc[0][i].direct:
            if(hero.position!=i):
                end=True


def enter():
    global hero,npc,end
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
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                hero.position += 1
                if hero.position==4:
                    hero.position = 3
                else:
                    hero.walk_mode=1
                    move_NPC()
                    Collosion()
            elif event.key == SDLK_LEFT:
                hero.position -= 1
                if hero.position==-1:
                    hero.position = 0
                else:
                    hero.walk_mode = 1
                    move_NPC()
                    Collosion()
            elif event.key == SDLK_UP:
                hero.walk_mode = 1
                move_NPC()
                Collosion()
            elif event.key == SDLK_ESCAPE:
                running = False

def update():
    hero.update()
    if(end):
        game_framework.change_state(title_state)
def draw():
    clear_canvas()
    #################################

    draw_NPC()
    hero.draw()

    #################################
    update_canvas()
    delay(0.1)