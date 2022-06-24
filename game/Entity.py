import pygame
from pygame.locals import *
from pygame.math import Vector2
from pygame import mixer
from Constants.constants import *
import random

'''
This is the base Entity Class. 
'''
class Entity():
    tag = "Default"
    bottom = 0

    entity_color = (0, 0, 0)
    sound = 0

    radius = 0

    right = 0
    left = 0

    def move(self,dt): 
        ranx = random.randrange(-5,5)
        rany = random.randrange(-5,5)
        self.position.y += dt * self.speed / rany
        self.position.x +=  dt * self.speed / ranx


       # self.up = self.position.y + (self.radius * random.randrange(0,10))
       # self.bottom = self.position.y - (self.radius * random.randrange(0,10))
        #self.right = self.position.x - (self.radius * random.randrange(0,10))
        #self.left = self.position.x + (self.radius * random.randrange(0,10))

    def collisions(self, enemies):
        if(self.position.y > 390):
            enemies.remove(self)
            enemies = enemies[:-1]
            self.sound.play()

    """
    The initaliser sets up the entity color and sound effect 
    """
    def initialiser(self, color):
        self.entity_color = color
        

    def draw(self, screen):
        pygame.draw.circle(screen, self.entity_color, (self.position.x, self.position.y), self.radius)