import pygame
import pygame_menu
from sys import exit
from main_menu.High_Score import HighScoreMenu
from main_menu.Information_Menu import InformationMenu
from game.Game_Play import game_play
from Constants.constants import *

pygame.init()
class Menu():
    """Main menu class"""
    def open_menu(self):

        #Establishing the main window itself
        self.main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.menu = pygame_menu.Menu('Welcome', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

        #Adding buttons to the menu
        self.menu.add.button("Play",self.start_game)
        self.menu.add.button("Instructions",self.show_information)
        self.menu.add.button("Highscores",self.open_high_scores)
        self.high_scores_session = HighScoreMenu(self.open_menu)
        self.top_score = self.high_scores_session.get_top_score()

        self.menu.add.button("Exit",pygame_menu.events.EXIT)

        self.menu.mainloop(self.main_surface)
        pygame.display.update()

    def show_information(self):
        """Method for opening the information window"""
        new_information_menu = InformationMenu(self.open_menu)
        new_information_menu.show_information()

    def open_high_scores(self):
        """Method for opening the high scores window""" 
        
        self.high_scores_session.show_high_scores()
        

    def start_game(self):
        """Method called when the user hits 'play' in main menu"""
        game_session = game_play(self.top_score,self.high_scores_session,self.open_menu)
        game_session.start_game_play()
        
        #game_session.end_game_V2()
        

#Create instance of begin_game menu class
new_menu = Menu()
#Initiate begin_game menu
new_menu.open_menu()


