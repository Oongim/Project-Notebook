import game_framework
import title_state
from pico2d import *


def enter(hero, event):
    pass


@staticmethod
def exit(hero, event):
    pass


@staticmethod
def do(hero):
    hero.frame = (hero.frame + 1)
    if (hero.frame == 19):
        game_framework.change_state(title_state)


@staticmethod
def draw(hero):
    hero.death[hero.frame].draw_now(400, 300)