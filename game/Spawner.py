import pygame
from game.Entity import Entity
from Constants.constants import *
from game.Entity_Type.Electron import Electron
import random
from game.Entity_Type.Protons import Protons
from game.Entity_Type.Light import Light

class Spawner():
    def __init__(self,screen):
        self.screen = screen

    def draw_particales(self, entity_alive, player):
        
        for i in range(len(entity_alive)):
            try:
                remove_particale = False
                entity_alive[i].draw(self.screen)
                entity_alive[i].move(8)
                entity_alive[i].checky()
                entity_alive[i].checkx()
                entity_alive[i].slow_down_over_time()
                entity_alive[i].check_speed()
                remove_particale = entity_alive[i].check_size()
                if remove_particale:
                    entity_alive[i].remove_entity(entity_alive,i)

            except:
                pass
        player.draw(self.screen)

    def timer(self,dt):
        self.time_elaspe = dt

    def spawner(self, entities_alive):
        
        random_int = random.randint(0, 2)
        if len(entities_alive) < 10:
            if random_int == 0:
                entity = Electron()
            elif random_int == 1:
                entity = Light()  
            else:
                entity = Protons()
                
            entities_alive.append(entity)

        self.time_elapsed = 0

    def remove_entity(self, entities_alive, remove_index):
        entities_alive.pop(remove_index)
    
   