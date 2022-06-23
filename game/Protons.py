from pygame.locals import *
from pygame.math import Vector2
from Constants.constants import *
from game.Entity import *
import random


'''
If you colode withe the electron entity you end up dieing
'''
class Protons(Entity):
    def __init__(self):
        self.speed = random.randrange(1, 5)
        self.position = Vector2()
        self.position.x = random.randrange(0, 720)
        self.position.y = 0

        self.initialiser((255, 0, 0))

        self.tag = "protons"

        self.radius = random.randrange(10, 30)