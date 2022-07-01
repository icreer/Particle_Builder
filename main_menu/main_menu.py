import pygame
import pygame_menu
from sys import exit
from High_Score import HighScores
from Information_Menu import InformationMenu
#from Game_Play import game_play
#from Constants.constants import *

pygame.init()
class Menu():
    """Main menu class"""
    def open_menu(self):

        #Establishing the main window itself
        self.main_surface = pygame.display.set_mode((600, 400))
        self.menu = pygame_menu.Menu('Welcome', 600, 400, theme=pygame_menu.themes.THEME_BLUE)

        #Adding buttons to the menu
        self.menu.add.button("Play",self.start_game)
        self.menu.add.button("Instructions",self.show_information)
        self.menu.add.button("Highscores",self.open_high_scores)
        self.menu.add.button("Exit",pygame_menu.events.EXIT)

        self.menu.mainloop(self.main_surface)
        pygame.display.update()

    def start_game(self):
        """Method called when the user hits 'play' in main menu"""
        print("Place holder for game start")
        #game_session = game_play()
        #game_session.start_game_play()

    def show_information(self):
        """Method for opening the information window"""
        new_information_menu = InformationMenu()
        new_information_menu.show_information()

    def open_high_scores(self):
        """Method for opening the high scores window"""
        high_scores_session = HighScores()
        high_scores_session.open_window()


#Create instance of begin_game menu class
new_menu = Menu()
#Initiate begin_game menu
new_menu.open_menu()


