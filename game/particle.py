#Object for a particle
class Player:
    """
    Purpose: create a player object and variables
    
    """
    def __init__(self, position, speed):
        """
        Purpose: create the base attributes and variables used within the class
        Parameters:
            self - an instance of the attributes of the player class
            position - the players loacation (x, y coordinates)
            speed - the x movement of the player
            can_jump - a true or false if the player is able to jump
        Return: 
            none
        """ 
        self.position = position
        self.speed = speed
    