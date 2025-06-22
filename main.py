import pygame
from constants import *

background_color = 'black'

def main():
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    pygame.init()
    
    # Set the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_active = True

    # Game loop
    while game_active:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

        screen.fill(background_color)
        pygame.display.flip()


if __name__ == "__main__":
    main()
