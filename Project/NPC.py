from pico2d import *
import random

class NPC:

    def __init__(self):
        self.x,self.y=0,0
        self.direct=0 #0=up 1= down 2= left 3= right
        self.font = load_font('ENCR10B.TTF', 16)
        self.form=random.randint(0, 8)
        if( self.form==0):
            self.image=load_image('Resource\\NPC\Girl1.png')
        elif ( self.form== 1):
            self.image = load_image('Resource\\NPC\Girl2.png')
        elif ( self.form == 2):
            self.image = load_image('Resource\\NPC\Girl3.png')
        elif ( self.form == 3):
            self.image = load_image('Resource\\NPC\Girl4.png')
        elif ( self.form == 4):
            self.image = load_image('Resource\\NPC\Girl5.png')
        elif ( self.form == 5):
            self.image = load_image('Resource\\NPC\Man1.png')
        elif ( self.form == 6):
            self.image = load_image('Resource\\NPC\Man2.png')
        elif ( self.form == 7):
            self.image = load_image('Resource\\NPC\Man3.png')
        elif ( self.form == 8):
            self.image = load_image('Resource\\NPC\Man4.png')

    def draw(self):
        if (self.direct == 6):
            self.image.clip_draw(0, 0, 64, 200, self.x, self.y)
        elif (self.direct != 5):
            self.image.clip_draw(self.direct*64,0,64,200,self.x,self.y)

    def change(self,curr,blank,pos):
        if(pos>3):
            if(curr<blank):
                self.x-=50
            elif(curr>blank):
                self.x+=50
