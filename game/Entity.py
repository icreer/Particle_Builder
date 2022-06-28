from html import entities
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
    x_direction = random.randrange(-1, 1)
    y_direction = random.randrange(-1, 1)
    radius = 0
    if x_direction == 0:
        x_direction = 1
    if y_direction == 0:
        y_direction = 1

    def move(self,dt): 
        ranx = random.randrange(-5,5)
        rany = random.randrange(-5,5)
        
        self.position.x += dt * self.speed * self.x_direction #/ranx
        self.position.y += dt *  self.speed * self.y_direction #/rany
       # print(self.position.y)
        #print(self.position.x)

        if self.position.y < 20 or self.position.y > SCREEN_HEIGHT:
            self.y_direction *= -1 
            print("pass")
            
        elif self.positon.x < 0 or self.position.x > SCREEN_WIDTH:
            self.x_direction *= -1
            print("pass") 
            

       # self.up = self.position.y + (self.radius * random.randrange(0,10))
       # self.bottom = self.position.y - (self.radius * random.randrange(0,10))
        #self.right = self.position.x - (self.radius * random.randrange(0,10))
        #self.left = self.position.x + (self.radius * random.randrange(0,10))

    
    """
    The initaliser sets up the entity color and sound effect 
    """
    def initialiser(self, color):
        self.entity_color = color
        

    def draw(self, screen):
        pygame.draw.circle(screen, self.entity_color, (self.position.x, self.position.y), self.radius)