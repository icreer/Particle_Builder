#Import statements for use in the main function
from particle import Particle

from update_particle import UpdateParticle
import constants
import pyray
from collision import Collision

#sets the players colors 
player_1_color = constants.RED
player_2_color = constants.BLACK

# Set our game to run at 60 frames-per-second
pyray.set_target_fps(60)

#initializes a window with the specified width, height, and title
pyray.init_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                  'Super Smash Bits - Raylib')


def main():
    """
    Purpose: Runs the main game functions
    Attributes:
        none
    """


    #main intialization of players onto the screen
    player = Particle(pyray.Vector2(400, 280), 0, False)

    #main game loop - will continuously run until the screen is closed or a player loses all lives
    while not pyray.window_should_close()  > 0:  # Detect window close button or ESC key
        
        # Update the frames
        delta_time = pyray.get_frame_time()

        #sets the canvas (window) to begin drawing (movement, attack, etc.)
        pyray.begin_drawing()

        #sets the seperate player keys into a their own lists
        keys_1 = [pyray.KEY_A, pyray.KEY_D, pyray.KEY_W, pyray.KEY_S, pyray.KEY_Q, pyray.KEY_E]
        

        #set the class updateplayer as variables
        game = UpdateParticle(player)

        #update the players using their location, keys being pressed, etc
        game.update_player(player, delta_time, keys_1, player_1_color)
        


    # player.direction = "right"
        #restarts the game
       
    # Draw
        #sets the background color
        pyray.clear_background(constants.LIGHTGRAY)

      
        #set player position values
        player_rect = pyray.Rectangle(
            int(player.position.x) - 20, 
            int(player.position.y) - 40,
            40, 40
        )

        #draw the players on screen
        pyray.draw_rectangle_rec(player_rect, player_1_color)
        
        #end the drawing sequence
        pyray.end_drawing()
   
    # Close window
    pyray.close_window()


#run the main file
main()