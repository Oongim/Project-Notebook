from pico2d import *
import random
class Map:
    def __init__(self):
        self.y=[300,900]
        self.image=load_image('Resource\\mapUP.png')
    def update(self,move_distance):
        for i in range(2):
            self.y[i] -= move_distance
            if self.y[i]==-300:
                self.y[i]=900
    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, self.y[0])
        self.image.clip_draw(0, 00, 800, 600, 400, self.y[1])
