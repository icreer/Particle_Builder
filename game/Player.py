#Object for a particle
from pygame import Vector2
from .Entity import Entity
from Constants.constants import *
import pygame
class Player(Entity):
    """
    Purpose: create a player object and variables
    
    """
    def __init__(self):
        """
        Purpose: create the base attributes and variables used within the class
        Parameters:
            self - an instance of the attributes of the player class
            position - the players loacation (x, y coordinates)
            speed - the x movement of the player
            can_jump - a true or false if the player is able to jump
        Return: 
            none
        """ 
        self.position = Vector2()
        self.position.x = SCREEN_WIDTH // 2
        self.position.y = SCREEN_HEIGHT // 2
        self.speed = 0
        self.initialiser(blue)
        self.tag = 'Player'
        self.radius = 15 
        self.charge = 2/3
        self.proton_count = 89
       

    def checky(self):
        if self.position.y >= SCREEN_HEIGHT - self.radius:
            self.position.y = SCREEN_HEIGHT - self.radius
        elif self.position.y < self.radius + 100:
            self.position.y = self.radius + 100

    def checkx(self):
        if self.position.x >= SCREEN_WIDTH - self.radius:
            self.position.x = SCREEN_WIDTH - self.radius
        elif self.position.x < self.radius:
            self.position.x = self.radius

    def move_left(self):
        self.position.x -= SPEED
        self.checkx()

    def move_right(self):
        self.position.x += SPEED
        self.checkx()

    def move_up(self):
        self.position.y -= SPEED
        self.checky()

    def move_down(self):
        self.position.y += SPEED
        self.checky()