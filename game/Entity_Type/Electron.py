
from pygame.locals import *
from pygame.math import Vector2
from Constants.constants import *
from game.Entity import *
import random


'''
If you collide with the electron entity you end up dying
'''
class Electron(Entity):
    def __init__(self):
        self.speed = random.randrange(1, 5)
        self.position = Vector2()
        self.position.x = random.randrange(0, SCREEN_WIDTH)
        self.position.y = random.randrange(0,SCREEN_HEIGHT)

        self.initialiser((0, 255, 0))

        self.tag = "electron"

        self.radius = random.randrange(10, 20)
