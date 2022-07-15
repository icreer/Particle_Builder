from pygame.locals import *
from pygame.math import Vector2
from Constants.constants import *
from game.Entity import *
import random


'''
When you collide with a Neutron your radius just gets bigger
'''
class Neutron(Entity):
    def __init__(self):
        self.speed =  1
        self.position = Vector2()
        self.position.x = random.randrange(0, SCREEN_WIDTH)
        self.position.y = random.randrange(105, SCREEN_HEIGHT)

        self.initialiser(white)

        self.tag = "Neutron"

        self.radius = 5
       