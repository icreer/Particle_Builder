from threading import main_thread
import pygame
import pygame_menu
#from main_menu import Menu
from Constants.constants import *


class InformationMenu():
    """Menu to display instructions and background for the game"""
    def show_information(self):
        """Initialize the information menu windoww"""
        print("Placeholder for information")
        self.information_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.information_menu = pygame_menu.Menu("Information",SCREEN_WIDTH,SCREEN_HEIGHT,onclose=self.open_original_menu)
        self.information_menu.add.label("Here's some information")
        for line in ["The particle builder is a game ",
                    "that is a mash-up of asteroid and 2048. "
                    ,"The overall goal is to build"
                    ,"largest stable atom that you can."
                    ,"Witch is a debated topic but "
                    ,"in nature is Uranium"
                    ,"with an atomic number of 92."
                    ,"The challenge of the game is" 
                    ,"building up to Uranium from a "
                    ,"single up quark. As you build up "
                    ,"to a Uranium Atom you can build an "
                    ,"unstable radioactive atom that"
                    ,"once can lead to your atom decaying"
                    ,"and you being set back in your"
                    ,"progress of building your atom."
                    ,"Another risk that the player has", 
                    "is that high energy light",
                    "waves can come in and destroy",
                    "your atom by chipping off a electron.",
                    "\n\nUse the arrow keys to move around",
                    "and avoid the light waves",
                    "and have fun learning!\n\n"]:
            self.information_menu.add.label(line)

        self.information_menu.add.button("Back to Main Menu",self.information_menu._back)
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