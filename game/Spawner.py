import pygame
from game.Entity import Entity
from Constants.constants import *
from game.Entity_Type.Electron import Electron
import random
from game.Entity_Type.Protons import Protons
from game.Entity_Type.Light import Light
from game.Entity_Type.Down_Quarks import Down_Quarks
from game.Entity_Type.Neutron import Neutron
from game.Entity_Type.Up_Quarks import Up_Quarks
from game.collision import KDT

"""
The Spawner Class deals with spawning and drawing all the entities on the screen.
"""
class Spawner():
    def __init__(self,screen):
        self.screen = screen
# This function deals with moving and drawing entities
    def draw_particales(self, entity_alive, player):
        particale_position = {}
        for i in range(len(entity_alive)):
            try:
                remove_particale = False
                entity_alive[i].draw(self.screen)
                entity_alive[i].move(8)
                entity_alive[i].checky()
                entity_alive[i].checkx()
                entity_alive[i].slow_down_over_time()
                entity_alive[i].check_speed()
                entity_alive[i].entity_position(particale_position,i)
                remove_particale = entity_alive[i].check_size()
                if remove_particale:
                    entity_alive[i].remove_entity(entity_alive,i, particale_position)

            except:
                pass
        player.draw(self.screen)

    def timer(self,dt):
        self.time_elaspe = dt
# This fuction deals with start of game spawning
    def spawner_start(self, entities_alive): 
        if len(entities_alive) < 2:   
            entity = Up_Quarks()
            entities_alive.append(entity)   
            entity = Down_Quarks()
            entities_alive.append(entity)        
# This fuction deals with the main part of the game spawning
    def spawner_main(self, entities_alive):
        
        random_int = random.randint(0, 10)
        if len(entities_alive) < 10:
            if random_int % 2 == 0 and random_int != 0:
                entity = Protons()
            elif random_int == 1:
                entity = Light() 
            elif random_int == 0:
                entity = Neutron() 
            else:
                entity = Electron()
                
            entities_alive.append(entity)

        self.time_elapsed = 0
# This fuction removies entities for the screen
    def remove_entity(self, entities_alive, remove_index):
        entities_alive.pop(remove_index)

    

                


    
   