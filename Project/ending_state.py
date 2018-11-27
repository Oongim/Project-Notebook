import game_framework
import title_state
import main_state
import random
import game_world
from pico2d import *
from Map import Ending_Map
class Judge:
    sprite_position = [[82, 140], [82, 140], [82, 140], [98, 140], [98, 140], [84, 0]]
    def __init__(self):
        self.image = [load_image('Resource\ending\\0.png'),
                 load_image('Resource\ending\\1.png'),
                 load_image('Resource\ending\\2.png'),
                 load_image('Resource\ending\\3.png'),
                 load_image('Resource\ending\\4.png')]
        self.frame = random.randint(0, 3)
        self.x=0
        self.y=580
    def draw(self):
        self.image[self.frame].clip_draw(0,0,Judge.sprite_position[self.frame][0], Judge.sprite_position[self.frame][1], self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 5


def enter():
    global judge,frame,back,NPC_LINE
    NPC_LINE = 4
    back=Ending_Map()
    game_world.add_object(back, 0)
    judge = [Judge() for i in range(4)]
    for i in range(4):
        judge[i].x=260+98*i
        game_world.add_object(judge[i], 0)


def exit():
    global judge,back
    main_state.remove_all_NPC_objectlist()
    main_state.game_world.remove_object(main_state.hero)
    game_world.remove_object(back)

    del(main_state.hero)
    del(main_state.npc)
    del (judge)
    del(back)

def update():
    global frame,NPC_LINE
    for i in range(4):
        judge[i].update()
    main_state.hero.update()
    if(main_state.hero.frame==10 and NPC_LINE!=0):
        back.y-=main_state.NPC_gap
        for i in range(4):
            judge[i].y -=main_state.NPC_gap
        for j in range(0, main_state.ROW_MAX):
            game_world.remove_object(main_state.npc[NPC_LINE][j])
        NPC_LINE-=1
def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()
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
            #elif (event.type) == (SDL_KEYDOWN):
                #game_framework.change_state(title_state)

def pause(): pass

def resume(): pass
