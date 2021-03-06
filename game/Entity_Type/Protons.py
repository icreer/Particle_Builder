from pygame.locals import *
from pygame.math import Vector2
from Constants.constants import *
from game.Entity import *
import random


'''
If you collide with the electron entity you end up dying
'''
class Protons(Entity):
    def __init__(self):
        self.speed = 1
        self.position = Vector2()
        self.position.x = random.randrange(0, SCREEN_WIDTH)
        self.position.y = random.randrange(130, SCREEN_HEIGHT)

        self.initialiser((255, 0, 0))

        self.tag = "protons"

        self.radius = random.randrange(25, 30)
        self.charge = 1
        
        
