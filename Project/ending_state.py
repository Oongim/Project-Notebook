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
        self.hammer = load_wav('Resource\\ending\\hammer.wav')
        self.hammer.set_volume(10)

    def hit_hammer(self):
        self.hammer.play()
    def draw(self):
        self.image[self.frame].clip_draw(0,0,Judge.sprite_position[self.frame][0], Judge.sprite_position[self.frame][1], self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 5
        if(self.frame==4):
            self.hit_hammer()

def enter():
    global judge,frame,back,NPC_LINE,font,font_y,hour,minute,ending_text,ending_text_size,opacify,press_space,fade_in,bgm
    font_y=870
    NPC_LINE = 4
    back=Ending_Map()
    game_world.add_object(back, 0)
    judge = [Judge() for i in range(4)]
    for i in range(4):
        judge[i].x=260+98*i
        game_world.add_object(judge[i], 0)
    font = load_font('Resource\ending\\DS-DIGIT.ttf', 150)

    hour=11+(30+main_state.frame_time//2)//60
    minute=((30+main_state.frame_time//2)%60)
    if(main_state.frame_time<120):
        ending_text=load_image('Resource\ending\\in_time.png')
        ending_text_size=[596,114]
    else:
        ending_text = load_image('Resource\ending\\over_time.png')
        ending_text_size = [640, 237]
    press_space=load_image('Resource\ending\\press_space.png')
    opacify=[1,0,0]
    fade_in=load_image('Resource\ending\\fade_in.png')
    bgm = load_music('Resource\\Music\\ending_bgm.mp3')
    bgm.set_volume(50)
    bgm.repeat_play()
def exit():
    global judge,back,font,ending_text,press_space,fade_in,bgm
    main_state.remove_all_NPC_objectlist()
    main_state.game_world.remove_object(main_state.hero)
    game_world.remove_object(back)

    del(main_state.hero)
    del(main_state.npc)
    del (judge)
    del(back)
    del (font)
    del(ending_text)
    del(press_space)
    del(fade_in)
    del(bgm)
def update():
    global frame,NPC_LINE,font_y,opacify
    if (opacify[0] >0.1):
        opacify[0] -= 0.1
        return
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
        font_y-=100
    if(NPC_LINE==0 and opacify[1]<0.9):
        opacify[1]+=0.1
    if(NPC_LINE==0 and opacify[1]>=0.9):
        opacify[2] += 0.1
def draw():
    global font_y,hour,minute,ending_text,opacify,fade_in,press_space,ending_text_size
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()
    font.draw(240, font_y, '%d' %hour , (255, 0, 0))
    font.draw(380, font_y, ':', (255, 0, 0))
    if(minute<10):
        font.draw(420, font_y, '0', (255, 0, 0))
        font.draw(490, font_y, '%d' % minute, (255, 0, 0))
    else:
        font.draw(420, font_y, '%d'%minute, (255, 0, 0))
    if (opacify[0] > 0.1):
        fade_in.opacify(opacify[0])
        fade_in.draw_now(400, 300)

    ending_text.opacify(opacify[1])
    ending_text.clip_draw(0,0,ending_text_size[0], ending_text_size[1], 400, 400)

    press_space.opacify(opacify[2])
    press_space.clip_draw(0,0,466, 87, 400, 300)

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
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)

def pause(): pass

def resume(): pass
