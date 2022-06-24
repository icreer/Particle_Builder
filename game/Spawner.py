import pygame
from game.Entity import Entity
from Constants.constants import *
from game.Electron import Electron
import random
from game.Protons import Protons

class Spawner():
    def __init__(self,screen):
        self.screen = screen

    def draw_particales(self, entity_alive):
        for i in range(len(entity_alive)):
            try:
                entity_alive[i].draw(self.screen)
                entity_alive[i].move(60)
            except:
                pass

    def timer(self,dt):
        self.time_elaspe = dt

    def spawner(self, entities_alive):
        
        random_int = random.randint(0, 4)
        if random_int == 0:
            entity = Electron()
            self.concurrent_entities += 1
        else:
            entity = Protons()
            self.concurrent_entities = 0
        entities_alive.append(entity)

        self.time_elapsed = 0