from tkinter import S
import pygame
from sys import exit
from Constants.constants import *
from game.Spawner import Spawner

import time

class game_play():
    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        self.dt *= 60
        self.previous_frame_time = time.time()

    def start_game_play(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        clock = pygame.time.Clock()
        entities = []
        spawner = Spawner(screen)
        while True:
           
            screen.fill((60,60,60))
            #pygame.draw.circle(screen,(200,200,0),(100,500),20)
            #enamy.draw(screen)
            spawner.spawner(entities)
            spawner.draw_particales(entities)
            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()
            clock.tick(60)
        