import pygame
from sys import exit
from Constants.constants import *
from game.Player import Player
from game.Spawner import Spawner
from game.HUD import HUD
import time
from game.collision import check_collision

"""
The Game play class deals the main game play. All of the game play really happens inside
of the start game play fucntion. The game play fuction uses stuff from the Player, Spawner
, collision and HUD classes.
"""
class game_play():
    def __init__(self,top_score):
        self.top_score = top_score

# This is the magic fuction that runs the game
    def start_game_play(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        font = pygame.font.Font("Constants/Fonts/Inter.ttf",32)
        pygame.display.set_caption(TITLE)
        clock = pygame.time.Clock()
        #sprites = pygame.sprite.Sprite()
        entities = []
        player = Player()
        spawner = Spawner(screen)
        hud = HUD(self.top_score)
        atomdiction = dict()
        gamestate = 0
        
        # This creates the Dictionary for the type of atoms that show up in the HUD
        with open("Constants/Atom list.csv") as atom:
            for line in atom:
                Atom_properdy = line.split(",")
                Atomic_number = Atom_properdy[0]
                Chemical_name = Atom_properdy[1]
                atomdiction[Atomic_number] = Chemical_name

        # This while loop is what the game happens in
        while True:
           
            screen.fill(black)
            # This condistions is what needs to be fulled or the game to switch from Qurts to main things in chemistry 
            if gamestate == 0:
                spawner.spawner_start(entities)
                if player.charge > .95  and player.charge < 1.05:
                    gamestate = 1
            else:
                spawner.spawner_main(entities)



            coordinates = []
            for entity in entities:
                coordinates.append(entity.get_coordinates())
            entities = check_collision(player, coordinates, entities)

            spawner.draw_particales(entities, player)
            hud.draw_hud(screen)
            hud.items_in_hud(screen,font, atomdiction, player)

            

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
            
            
            if player.proton_count == 90:
                break
                

            pygame.display.update()
            self.clock.tick(60)

        self.end_game()

    def end_game(self):
        while True:
            self.screen.fill(black)
            pygame.display.update()
            self.end_of_game = time.time()
            print(self.end_of_game - self.start_of_game)

        
        
