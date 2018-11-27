from pico2d import *
import random
import game_framework
import game_world
import ending_state
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
    def update(self,y):
        self.y = y+260

    def plus_count(self):
        self.count += 1
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
END_COUNT=1
NPC_gap=100

def remove_all_NPC_objectlist():
    for i in range(0, COLUMN_MAX):  # Set NPC position
        for j in range(0, ROW_MAX):
            game_world.remove_object(npc[i][j])

def normalize_NPC_position():
    for i in range(0, COLUMN_MAX):  # Set NPC position
        for j in range(0, ROW_MAX):
            if(npc[i][j].state!=CHANGE_NPC):
                npc[i][j].x = NPC_gap * j + 250
            npc[i][j].y = NPC_gap * i + 100
            game_world.add_object(npc[i][j], COLUMN_MAX-i)
def initialize_NPC(start_position):
    empty_position = start_position

    for i in range(0, COLUMN_MAX):  #Set Empty position
        npc[i][empty_position].state = EMPTY
        empty_position = random.randint(max(0, empty_position-1), min(3,empty_position+1))

    normalize_NPC_position()


def draw_NPC():
    for i in range(COLUMN_MAX-1,-1,-1):
        for j in range(0,ROW_MAX):
            if(npc[i][j].y!=0):
                npc[i][j].draw()


def choice_Change_NPC(empty_position):
    changed_position = random.randint(max(0, empty_position - 1), min(3, empty_position + 1))
    while(empty_position==changed_position):
        changed_position = random.randint(max(0, empty_position - 1), min(3, empty_position + 1))
    npc[COLUMN_MAX - 1][changed_position].state = CHANGE_NPC
    npc[COLUMN_MAX - 1][changed_position].x+=(empty_position-changed_position)*NPC_gap

def make_new_NPC_row(empty_position):
    global level_of_difficulty
    for i in range(0, ROW_MAX):
        npc[COLUMN_MAX-1][i].form = random.randint(0, 8)
        npc[COLUMN_MAX-1][i].state = UP_DIRECTION
        game_world.remove_object(npc[COLUMN_MAX-1][i])

    next_empty_position = random.randint(max(0, empty_position - 1), min(3, empty_position + 1))
    npc[COLUMN_MAX-1][next_empty_position].state = EMPTY

    if ((cnt.count ) % level_of_difficulty==0and cnt.count!=0):
        choice_Change_NPC(next_empty_position)
def regulate_level():
    global level_of_difficulty
    if (cnt.count == END_COUNT):
        game_framework.change_state(ending_state)
    elif(cnt.count >= 170):
        level_of_difficulty =1
    elif (cnt.count >= 140):
        level_of_difficulty = 2
    elif (cnt.count >= 100):
        level_of_difficulty = 3
    elif(cnt.count >= 50):
        level_of_difficulty=4
    elif (cnt.count >= 25):
        level_of_difficulty = 5


def change_NPC_column():

    for i in range(1,COLUMN_MAX):      #move NPC list position column minus 1
        npc[i-1], npc[i]=npc[i],npc[i-1]
    if (cnt.count <= END_COUNT):
        for i in range(0,ROW_MAX):
            if (npc[COLUMN_MAX-2][i].state==EMPTY):
                make_new_NPC_row(i)
    else:
        make_new_NPC_row(0)
    remove_all_NPC_objectlist()
    normalize_NPC_position()
    print('%d, %d, %d, %d  ' % (npc[0][0].state,npc[0][1].state,npc[0][2].state,npc[0][3].state))

def move_NPC(move_distance):
    disappear_postion=-100
    appear_positon=600

    for i in range(0, COLUMN_MAX):  #move NPC column Position
        for j in range(0,ROW_MAX):
            npc[i][j].y-=move_distance
            npc[i][j].y=max((i-1)*100+100,npc[i][j].y)
            if npc[i][j].y==disappear_postion:
                npc[i][j].y=appear_positon
            if (npc[i][j].state == CHANGE_NPC):
                if (npc[i][max(0,j - 1)].state == EMPTY):
                    npc[i][j].change(j, j - 1, i,move_distance)
                elif (npc[i][min(3,j + 1)].state == EMPTY):
                    npc[i][j].change(j, j + 1,i ,move_distance)


def enter():
    global hero,npc,end,map,cnt,level_of_difficulty

    level_of_difficulty=25

    map=Map()
    cnt=Count()
    hero = Hero()
    npc = [[NPC() for i in range(4)] for i in range(7)]

    start_positon=2
    end = False
    initialize_NPC(start_positon)  # 빈칸 생성

    game_world.add_object(hero,COLUMN_MAX)
    game_world.add_object(map,0)
    game_world.add_object(cnt, 0)
def exit():
    global hero, npc,map
    remove_all_NPC_objectlist()
    game_world.remove_object(hero)
    game_world.remove_object(map)
    game_world.remove_object(cnt)

    del(hero)
    del(npc)
    del(map)



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
    regulate_level()
def draw():
    clear_canvas()
    #################################
    for game_object in game_world.all_objects():
        game_object.draw()
    #################################
    update_canvas()
    delay(0.1)
