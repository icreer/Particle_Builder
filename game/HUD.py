import pygame
from Constants.constants import *

class HUD():
    #def __init__(self,screen):
     #   self.screen = screen
    def draw_hud(self,screen):
        pygame.draw.rect(screen,gray,pygame.Rect(0,0,SCREEN_WIDTH,100))

    def items_in_hud(self,screen, font, atomdiction):
        charge = font.render("Charge:" + str(int(0.0)), True, white)
        type_of_particale = font.render("Partical type: " + str(atomdiction["2"]), True, white)
        number_of_protons = font.render("Proton Count: " + str(int(1.0)), True, white)
        high_score = font.render("High Score: "+ str(), True, white)
        screen.blit(type_of_particale,(10,10))
        screen.blit(charge,(500,10))
        screen.blit(number_of_protons,(700,10))
        screen.blit(high_score,(1200,10))