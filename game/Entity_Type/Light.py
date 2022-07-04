from pygame.locals import *
from pygame.math import Vector2
from Constants.constants import *
from game.Entity import *
import random


'''
If you colode withe the electron entity you end up dieing
'''
class Light(Entity):
    def __init__(self):
        self.speed = random.randrange(3, 6)
        self.position = Vector2()
        self.position.x = random.randrange(0, SCREEN_WIDTH)
        self.position.y = random.randrange(0, SCREEN_HEIGHT)

        self.initialiser((255, 255, 0))

        self.tag = "light"

        self.radius = 5