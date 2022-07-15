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
        
        self.position.x += dt * self.speed * self.x_direction #/ranx
        self.position.y += dt *  self.speed * self.y_direction #/rany
       

    
    """
    The initaliser sets up the entity color and sound effect 
    """
    def initialiser(self, color):
        self.entity_color = color
        

    def draw(self, screen):
       # print(self.tag)
       # if self.tag =="protons4":
            
            #self.sprites.image = pygame.image.load("game/Entity_Type/Entity_Images/Protons.png").convert_alpha()

           # self.sprites.rect = self.sprites.image.get_rect()
            #self.sprites.image = pygame.transform.scale(self.sprites.image,(int(self.radius * 2), int(self.radius * 2)))
           # screen.blit(self.sprites,(self.position.x,self.position.y))
        #elif self.tag == "electron4":
            
           # self.sprites.image = pygame.image.load("game/Entity_Type/Entity_Images/Electron.png").convert_alpha()

           # self.sprites.rect = self.sprites.image.get_rect()
           # self.sprites.image = pygame.transform.scale(self.sprites.image,(int(self.radius * 2), int(self.radius * 2)))
          #  screen.blit(self.sprites,(self.position.x,self.position.y))
       # else:
            pygame.draw.circle(screen, self.entity_color, (self.position.x, self.position.y), self.radius)
        
    def checky(self):
        if self.position.y < 100 + self.radius or self.position.y > SCREEN_HEIGHT - self.radius:
            self.y_direction *= -1
        
    def checkx(self):
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH:
            self.x_direction *= -1    

    def slow_down_over_time(self):
        self.speed -= .50 * self.speed 
        if self.tag == "light":
            self.speed -= 1e-3 * self.speed
        elif self.tag == "protons":
            self.speed -= .001 * self.speed
        elif self.tag == "electron":
            self.speed -= .001 * self.speed 
        else:
            self.speed -= .001 * self.speed 

    def check_speed(self):
        if self.speed <= 0.5:
            self.speed = 0
            self.radius -= .25 * self.radius 

    def check_size(self):
        if self.radius <= 1:
            return True
        else:
            return False

    def remove_entity(self, entities_alive, remove_index, position):
        entities_alive.pop(remove_index)
        position.pop(remove_index)
        
    def entity_position(self, position, index):
        position[index] = [self.position.x, self.position.y]

    
    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius
        
    def get_coordinates(self):
        return [self.position.x, self.position.y]        
