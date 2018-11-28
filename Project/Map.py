from pico2d import *

class Map:
    def __init__(self):
        self.y=[300,900]
        self.position_num=3
        self.image=load_image('Resource\\mapUp.png')
        self.bgm=load_music('Resource\\Music\\main_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def update(self,move_distance):
        for i in range(2):
            self.y[i] -= move_distance
            self.y[i]=max((self.position_num-1+(i*6))*100,self.y[i])
            if self.y[i]<=-300:
                self.y[i]=900
    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, self.y[0])
        self.image.clip_draw(0, 00, 800, 600, 400, self.y[1])
    def normalize_position(self):
        for i in range(2):
            self.y[i] = (self.position_num-1+(i*6))*100

        self.position_num-=1
        if(self.position_num==-3):
            self.position_num = 3

class Ending_Map:
    def __init__(self):
        self.y = 550
        self.image = load_image('Resource\ending\Test2.png')

    def update(self):
        pass
    def draw(self):
        #self.image.draw_now(400,self.y)
        self.image.clip_draw(0, 0, 800, 1500, 400, self.y)