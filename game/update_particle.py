#CODE IS NOT COMPLETE, OR NEAR WORKING. I STOLE THIS CODE FROM A PREVIOUS PROJECT OF MINE, AND DIDN'T HAVE TIME TO FIX EVERYTHING


#updates the player and other particle positionsimport pyray
from multiprocessing import Event
import Constants.constants as constants
import pygame
class UpdateParticle:
    """
    Purpose: create a class which can be utilized to update the player 
        
    """
    def __init__(self, player):
        """
        Purpose: create the base attributes and variables used within the class
        Parameters:
            self - an instance of the attributes of the player class
            player - str used in the main file to help know which player is linked to which variable
        Return:
            none 
        """
        self.y = 0

    def update_player(self, player, delta, keys, player_color):
        """
        Purpose: update the player based upon actions and keys pressed during the game
        Parameters:
            self - an instance of the attributes of the player class
            player - str containing the player class for player 1 or for player 2
            env items - list of the enviroment items (the platforms)
            delta - the frame time of the game (time)
            keys - a list of the keys that the player can press
            player color - the color of the player
        Return:
            none 
        """
        
        #left (a and j)
        if pygame.K_a == pygame.KEYDOWN or pygame.K_j == pygame.KEYDOWN:
            player.position.x -= constants.PLAYER_HOR_SPD * delta
            

        #right (d and l)
        if pygame.K_d == pygame.KEYDOWN or pygame.K_l == pygame.KEYDOWN:
            player.position.x += constants.PLAYER_HOR_SPD * delta
           
            
        #jump (w and i)
        if pygame.K_w == pygame.KEYDOWN or pygame.K_i == pygame.KEYDOWN:
            player.position.y -= constants.PLAYER_VERT_SPD * delta
        
        #sheild (s and k)
        
        if pygame.K_s == pygame.KEYDOWN or pygame.K_k == pygame.KEYDOWN:
            player.position.y += constants.PLAYER_VERT_SPD * delta
           
            

        
