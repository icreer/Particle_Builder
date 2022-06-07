import pygame
import pygame_menu
from sys import exit
from constants import *


def begin_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)

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
        begin_game()

    def show_information(self):
        """Method for opening the information window"""
        new_information_menu = InformationMenu()
        new_information_menu.show_information()

    def open_high_scores(self):
        """Method for opening the high scores window"""
        high_scores_session = HighScores()
        high_scores_session.open_window()

class InformationMenu():
    """Menu to display instructions and background for the game"""
    def show_information(self):
        """Initialize the information menu windoww"""
        print("Placeholder for information")
        self.information_surface = pygame.display.set_mode((600,400))

        self.information_menu = pygame_menu.Menu("Information",600,400,onclose=self.open_original_menu)
        self.information_menu.add.label("Here's some information")
        self.information_menu.add.button("Exit",self.open_original_menu)
        self.information_menu.mainloop(self.information_surface)

    def open_original_menu(self):
        """Close information window and return to begin_game menu"""
        print("opening")
        menu = Menu()
        menu.open_menu()

class HighScores():
    """Class for accessing and displaying all previous high scores"""
    def __init__(self):
        print("hi there, initiating")

    def open_window(self):
        print("Opening window")


#Create instance of begin_game menu class
new_menu = Menu()
#Initiate begin_game menu
new_menu.open_menu()


