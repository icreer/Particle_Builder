from tkinter import S
import pygame
from sys import exit
from Constants.constants import *
from game.Player import Player
from game.Spawner import Spawner
from game.HUD import HUD
import time

class game_play():
    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        self.dt *= 60
        self.previous_frame_time = time.time()

    def start_game_play(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        font = pygame.font.Font("Constants/Fonts/Inter.ttf",32)
        pygame.display.set_caption(TITLE)
        clock = pygame.time.Clock()
        #sprites = pygame.sprite.Sprite()
        entities = []
        player = Player()
        spawner = Spawner(screen)
        hud = HUD()
        atomdiction = dict()
        with open("Constants/Atom list.csv") as atom:
            for line in atom:
                Atom_properdy = line.split(",")
                Atomic_number = Atom_properdy[0]
                Chemical_name = Atom_properdy[1]
                atomdiction[Atomic_number] = Chemical_name

        
        while True:
           
            screen.fill(black)
            
            spawner.spawner(entities)
            spawner.draw_particales(entities, player)
            hud.draw_hud(screen)
            hud.items_in_hud(screen,font, atomdiction)
            
            keys = pygame.key.get_pressed()  #checking pressed keys
            if keys[pygame.K_w]:
                player.move_up()
            if keys[pygame.K_s]:
                player.move_down()
            if keys[pygame.K_a]:
                player.move_left()
            if keys[pygame.K_d]:
                player.move_right()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    

            pygame.display.update()
            clock.tick(60)
        