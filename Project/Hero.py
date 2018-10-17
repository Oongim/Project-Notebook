from pico2d import *
import random
class Hero:
    def __init__(self ):
        self.x,self.y=0,0
        self.frame=0
        self.position=2
        self.walk_mode=0   #0=idle 1= up 2= down 3= Lup 4= Left 5= Ldown 6=Rup 7=Right 8=Rdown
        self.idle=load_image('Resource\hero\idle.png')
        self.move=load_image('Resource\hero\Walk.png')
    def update(self):
        self.x = 100 * self.position + 250
        self.y = 100
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
