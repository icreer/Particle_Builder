#CODE IS NOT COMPLETE, OR NEAR WORKING. I STOLE THIS CODE FROM A PREVIOUS PROJECT OF MINE, AND DIN"T HAVE TIME TO FIX EVERYTHING


#updates the player and other particle positionsimport pyray
import constants
import pyray
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
        if pyray.is_key_down(keys[0]) :
            player.position.x -= constants.PLAYER_HOR_SPD * delta
            

        #right (d and l)
        if pyray.is_key_down(keys[1]) :
            player.position.x += constants.PLAYER_HOR_SPD * delta
           
            
        #jump (w and i)
        if pyray.is_key_down(keys[2]):
            player.position.y -= constants.PLAYER_VERT_SPD * delta
        
        #sheild (s and k)
        
        if pyray.is_key_down(keys[3]):
            player.position.y += constants.PLAYER_VERT_SPD * delta
           
            

        
