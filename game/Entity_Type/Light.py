from pygame.locals import *
from pygame.math import Vector2
from Constants.constants import *
from game.Entity import *
import random


'''
If you collide with the electron entity you end up dying
'''
class Light(Entity):
    def __init__(self):
        self.speed =  2
        self.position = Vector2()
        self.position.x = random.randrange(0, SCREEN_WIDTH)
        self.position.y = random.randrange(100, SCREEN_HEIGHT)

        self.initialiser((255, 255, 0))

        self.tag = "light"

        self.radius = 5
        self.charge = 0
        
