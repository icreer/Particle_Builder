import pygame
import pygame_menu
from sys import exit
from Constants.constants import *
from game.Player import Player
from game.Spawner import Spawner
from game.HUD import HUD
from main_menu.High_Score import HighScoresData
import time
from game.collision import check_collision

"""
The Game play class deals the main game play. All of the game play really happens inside
of the start game play fucntion. The game play fuction uses stuff from the Player, Spawner
, collision and HUD classes.
"""
class game_play():
    def __init__(self,top_score,highscore_session,back_to_menu_function):
        self.top_score = top_score
        self.highscores_session = highscore_session
        self.back_to_menu_function = back_to_menu_function

# This is the magic fuction that runs the game
    def start_game_play(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font("Constants/Fonts/Inter.ttf",32)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        #sprites = pygame.sprite.Sprite()
        self.start_game_time = time.time()
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
            hud.items_in_hud(screen,self.font, atomdiction, player)

            

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
            self.clock.tick(60)
            
            
            if player.proton_count == 92:
                break
                

            pygame.display.update()
            self.clock.tick(60)
        end_game(self.start_game_time,self.font,self.top_score)
       # self.end_game_V2()


    def end_game_V2(self):
        
        end_of_game = time.time()
        self.total_time = end_of_game - self.start_game_time
        print()
        print(type(self.total_time))
        if self.highscores_session.high_scores_data.check_in_high_scores(self.total_time):
       
            #Open menu to add new high score name and score itself'
            high_score_input_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
            self.high_score_input_screen = pygame_menu.Menu("New Highscore",SCREEN_WIDTH,SCREEN_HEIGHT)
            self.high_score_input_screen.add.label("NEW HIGHSCORE")
            self.user_name_input = self.high_score_input_screen.add.text_input("Username: ")
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
                score_card = self.font.render("The time you took was: "+ str(round(end_of_game - self.start_game_time,2)) + " seconds", True, white)    
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
        self.highscores_session.high_scores_data.update_top_ten(self.total_time,self.user_name_input.get_value())
        print("Step 1 Done")
        pygame.quit()
        print("Step 2 aaaaaaand done")
        pygame.init()
        self.back_to_menu_function()
        print("Step done aaaand done")

def end_game(start_game_time, font, high_score):
    clock = pygame.time.Clock()
    end_of_game = time.time()
    end_screen = True
    player_score = end_of_game - start_game_time
    high_score_database = HighScoresData()
    does_make_in_top_ten = False
    does_make_in_top_100 = False
    user_id = ""
    input_rect = pygame.Rect(SCREEN_WIDTH/3,SCREEN_HEIGHT/3, 300, 64) 
    has_enter_in_id = False
    active = False
    rect_color = gray
    while end_screen:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(black)
        score_card = font.render("The time you took was: "+ str(round(player_score,2)) + " seconds", True, white)
        high_scores = font.render("The high score is " + str(high_score), True, white)    
        press_any_button = font.render("Press any button to continue", True, white)
        user_id_message = font.render("Please enter in your User id", True, white)

        screen.blit(score_card , (SCREEN_WIDTH/4, 50))
        screen.blit(user_id_message,(SCREEN_WIDTH/4, 200))


        screen.blit(press_any_button, (SCREEN_WIDTH/4, SCREEN_HEIGHT/1.5))
        screen.blit(high_scores,(SCREEN_WIDTH/4, SCREEN_HEIGHT/2) )

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_id = user_id[:-1]
                    elif event.key == pygame.K_RETURN:
                        has_enter_in_id = True
                        does_make_in_top_ten = high_score_database.update_top_ten(player_score,user_id)
                        if not does_make_in_top_ten:
                            does_make_in_top_100 = high_score_database.update_top_100(player_score,user_id)
                    elif has_enter_in_id:
                        end_screen = False
                    else: 
                        user_id += event.unicode
                    

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else: 
                        active = False



        if active:
            rect_color = SkyBlue
        else:
            rect_color = gray
        press_any_button = font.render("Press any button to continue", True, white)
        user_id_message = font.render("Please enter in your User id", True, white)
        user_text = font.render(user_id,True,white)
        

        if not has_enter_in_id:
            pygame.draw.rect(screen,rect_color, input_rect)
            screen.blit(user_text,(input_rect.x+5,input_rect.y+5))
            screen.blit(user_id_message,(SCREEN_WIDTH/4, 200))
            
            input_rect.w = max(100, user_text.get_width()+10)

        else:
            screen.blit(press_any_button, (SCREEN_WIDTH/4, SCREEN_HEIGHT/1.5))
        
        pygame.display.update()

        clock.tick(60)
           

    

        
    