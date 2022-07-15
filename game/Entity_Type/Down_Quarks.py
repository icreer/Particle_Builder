from pygame.locals import *
from pygame.math import Vector2
from Constants.constants import *
from game.Entity import *
import random


'''
In the start game you need to collide with one up Quark and one down Quarks to move on to the main game
'''
class Down_Quarks(Entity):
    def __init__(self):
        self.speed =  1.2
        self.position = Vector2()
        self.position.x = random.randrange(0, SCREEN_WIDTH)
        self.position.y = random.randrange(105, SCREEN_HEIGHT)

        self.initialiser(green)

        self.tag = "Down_Quarks"

        self.radius = 15
       