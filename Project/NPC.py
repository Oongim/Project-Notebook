from pico2d import *
import random

UP_DIRECTION,DOWN_DIRECTION,LEFT_DIRECTION,RIGHT_DIRECTION,EMPTY,CHANGE_NPC =range(6)

class NPC:
    sprite=[None for i in range(9)]

    def __init__(self):
        self.x,self.y=0,0
        self.state=UP_DIRECTION
        self.form=random.randint(0, len(NPC.sprite)-1)
        if (NPC.sprite[self.form] == None):
            if (self.form == 0):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Girl1.png')
            elif (self.form == 1):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Girl2.png')
            elif (self.form == 2):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Girl3.png')
            elif (self.form == 3):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Girl4.png')
            elif (self.form == 4):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Girl5.png')
            elif (self.form == 5):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Man1.png')
            elif (self.form == 6):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Man2.png')
            elif (self.form == 7):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Man3.png')
            elif (self.form == 8):
                NPC.sprite[self.form] = load_image('Resource\\NPC\Man4.png')
        self.image = NPC.sprite[self.form]

    def draw(self):
        if (self.state == CHANGE_NPC):
            self.image.clip_draw(0,0,64,200,self.x,self.y)
        elif (self.state != EMPTY):
            self.image.clip_draw(self.state*64,0,64,200,self.x,self.y)

    def change(self,current_pos,empty,row_pos,move_distance):
        if (current_pos < empty):
            self.x =max(current_pos*100+250,self.x-move_distance/4)
        elif (current_pos > empty):
            self.x = min( self.x + move_distance/4,current_pos * 100 + 250)
