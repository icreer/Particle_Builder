import pygame
from sys import exit
from Constants.constants import *

class game_play():
    def start_game_play(self):
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
        