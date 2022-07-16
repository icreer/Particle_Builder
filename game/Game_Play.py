from tkinter import S
import pygame
from sys import exit
from Constants.constants import *
from game.Player import Player
from game.Spawner import Spawner
from game.HUD import HUD
import time
from game.collision import check_collision
import time
import pygame_menu

class game_play():
    def __init__(self,top_score,highscore_session,back_to_menu_function):
        self.top_score = top_score
        self.highscores_session = highscore_session
        self.back_to_menu_function = back_to_menu_function

    def calculate_deltatime(self):
        self.dt = time.time() - self.previous_frame_time
        self.dt *= 60
        self.previous_frame_time = time.time()

    def start_game_play(self):
        self.start_of_game = time.time()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font("Constants/Fonts/Inter.ttf",32)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        #sprites = pygame.sprite.Sprite()
        entities = []
        player = Player()
        spawner = Spawner(self.screen)
        hud = HUD(self.top_score)
        atomdiction = dict()
        gamestate = 0
        
        with open("Constants/Atom list.csv") as atom:
            for line in atom:
                Atom_properdy = line.split(",")
                Atomic_number = Atom_properdy[0]
                Chemical_name = Atom_properdy[1]
                atomdiction[Atomic_number] = Chemical_name

        while True:
            self.screen.fill(black)
            
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
            hud.draw_hud(self.screen)
            hud.items_in_hud(self.screen,self.font, atomdiction, player)

            

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
                    
            if player.proton_count == 90:
                break
                

            pygame.display.update()
            self.clock.tick(60)

        self.end_game()

    def end_game(self):
        
        end_of_game = time.time()
        self.total_time = end_of_game - self.start_of_game
        print()
        print(type(self.total_time))
        if self.highscores_session.high_scores_data.check_in_high_scores(self.total_time):
            #Open menu to add new high score name and score itself'
            high_score_input_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
            self.high_score_input_screen = pygame_menu.Menu("New Highscore",SCREEN_WIDTH,SCREEN_HEIGHT)
            self.high_score_input_screen.add.label("NEW HIGHSCORE")
            self.user_name_input = self.high_score_input_screen.add.text_input("Username:")
            self.enter_user_name_button = self.high_score_input_screen.add.button("Enter",self.enter_new_user_name)
            self.high_score_input_screen.mainloop(high_score_input_surface)

            """
            self.highscores_session.update_top_ten(score,name)
            """
        else:
            end_of_game = time.time()
            end_screen = True
            while end_screen:
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                screen.fill(black)
                score_card = self.font.render("The time you took was: "+ str(round(end_of_game - start_game_time,2)) + " seconds", True, white)    
                press_any_button = self.font.render("Press any button to continue", True, white)
                screen.blit(score_card , (SCREEN_WIDTH/4, SCREEN_HEIGHT/2))
                screen.blit(press_any_button, (SCREEN_WIDTH/3, SCREEN_HEIGHT/1.5))

            
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            end_screen = False
                pygame.display.update()
                

    def enter_new_user_name(self):
        print("ok")
        self.highscores_session.high_scores_data.update_top_100(self.total_time,self.user_name_input.get_value())
        print("Step 1 Done")
        pygame.quit()
        print("Step 2 aaaaaaand done")
        pygame.init()
        self.back_to_menu_function()
        print("Step done aaaand done")

        