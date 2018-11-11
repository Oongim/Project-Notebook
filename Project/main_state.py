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

UP_DIRECTION,DOWN_DIRECTION,LEFT_DIRECTION,RIGHT_DIRECTION,EMPTY,CHANGE_NPC =range(6)

COLUMN_MAX=7
ROW_MAX=4

NPC_gap=100

def initialize_NPC(start_position):
    empty_position = start_position

    for i in range(0, COLUMN_MAX):  #Set Empty position
        npc[i][empty_position].state = EMPTY
        empty_position = random.randint(max(0, empty_position-1), min(3,empty_position+1))

    for i in range(0, COLUMN_MAX):  #Set NPC position
        for j in range(0,ROW_MAX):
            npc[i][j].x=NPC_gap*j + 250
            npc[i][j].y=NPC_gap*i + 100


def draw_NPC():
    for i in range(COLUMN_MAX-1,-1,-1):
        for j in range(0,ROW_MAX):
            npc[i][j].draw()


def choice_Change_NPC(empty_position):
    changed_position = random.randint(max(0, empty_position - 1), min(3, empty_position + 1))
    while(empty_position==changed_position):
        changed_position = random.randint(max(0, empty_position - 1), min(3, empty_position + 1))
    npc[COLUMN_MAX - 1][changed_position].state = CHANGE_NPC
    npc[COLUMN_MAX - 1][changed_position].x+=(empty_position-changed_position)*NPC_gap

def make_new_NPC_row(empty_position):
    for i in range(0, ROW_MAX):
        npc[COLUMN_MAX-1][i].form = random.randint(0, 8)
        npc[COLUMN_MAX-1][i].state = UP_DIRECTION

    next_empty_position = random.randint(max(0, empty_position - 1), min(3, empty_position + 1))
    npc[COLUMN_MAX-1][next_empty_position].state = EMPTY

    if(cnt.count>=25):
        if ((cnt.count ) % 5==0):
           choice_Change_NPC(empty_position)

def change_NPC_column():
    for i in range(1,COLUMN_MAX):      #move NPC list position column minus 1
        npc[i-1], npc[i]=npc[i],npc[i-1]
    for i in range(0,ROW_MAX):
        print(i)
        if (npc[COLUMN_MAX-2][i].state==EMPTY):
            make_new_NPC_row(i)

def move_NPC():
    disappear_postion=-100
    appear_positon=600
    cnt.update()
    for i in range(0, COLUMN_MAX):  #move NPC column Position
        for j in range(0,ROW_MAX):
            npc[i][j].y-=NPC_gap
            if npc[i][j].y==disappear_postion:
                npc[i][j].y=appear_positon
            if (npc[i][j].state == CHANGE_NPC):
                if (npc[i][j - 1].state == EMPTY):
                    npc[i][j].change(j, j - 1, i)
                elif (npc[i][j + 1].state == EMPTY):
                    npc[i][j].change(j, j + 1, i)
    change_NPC_column()




def enter():
    global hero,npc,end,map,cnt

    map=Map()
    cnt=Count()
    hero = Hero()
    npc = [[NPC() for i in range(4)] for i in range(7)]

    start_positon=2
    end = False
    initialize_NPC(start_positon)  # 빈칸 생성

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
