import pygame
from Constants.constants import *

class HUD():
    def __init__(self,top_score):
        self.top_score = top_score
    #def __init__(self,screen):
     #   self.screen = screen
    def draw_hud(self,screen):
        pygame.draw.rect(screen,gray,pygame.Rect(0,0,SCREEN_WIDTH,100))

    def items_in_hud(self,screen, font, atomdiction, player):
        charge = font.render("Charge: " + str(round(player.charge, 2)), True, white)
        type_of_particale = font.render("Particle Type: " + str(atomdiction["2"]), True, white)
        number_of_protons = font.render("Proton Count: " + str(int(0)), True, white)
        high_score = font.render("High Score: "+ str(self.top_score), True, white)
        screen.blit(type_of_particale,(10,10))
        screen.blit(charge,(500,10))
        screen.blit(number_of_protons,(800,10))
        screen.blit(high_score,(1200,10))