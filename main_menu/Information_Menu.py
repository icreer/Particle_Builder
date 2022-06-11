from threading import main_thread
import pygame
import pygame_menu
#from main_menu import Menu

class InformationMenu():
    """Menu to display instructions and background for the game"""
    def show_information(self):
        """Initialize the information menu windoww"""
        print("Placeholder for information")
        self.information_surface = pygame.display.set_mode((600,400))

        self.information_menu = pygame_menu.Menu("Information",600,400,onclose=self.open_original_menu)
        self.information_menu.add.label("Here's some information")
        """
        The player can just press the x to go back to the main menu
        """
        #self.information_menu.add.button("Exit",self.open_original_menu)
        self.information_menu.mainloop(self.information_surface)

    def open_original_menu(self):
        """Close information window and return to begin_game menu"""
        print("opening")
       # menu = Menu()
       # menu.open_menu()