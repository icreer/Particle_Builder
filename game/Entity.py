import pygame
from pygame.locals import *
from pygame.math import Vector2
from pygame import mixer
from Constants.constants import *


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

    def move(self, dt):
        self.position.y += dt * self.speed
        self.position.x += dt * self.speed
        self.bottom = self.position.y + (self.radius * 2)
        self.right = self.position.x + (self.radius * 2)
        self.left = self.position.x

    def collisions(self, enemies):
        if(self.position.y > 390):
            enemies.remove(self)
            enemies = enemies[:-1]
            self.sound.play()

    """
    The initaliser sets up the entity color and sound effect 
    """
    def initialiser(self, color, sfx_path):
        self.entity_color = color
        self.sound = mixer.Sound(sfx_path)

    def draw(self, screen):
        pygame.draw.circle(screen, self.entity_color, (self.position.x, self.position.y), self.radius)