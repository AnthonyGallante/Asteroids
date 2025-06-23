import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

background_color = 'black'

def main():
    
    print('Starting Asteroids!')
    game_active = True
    pygame.init()

    print('Updating Groups')
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    Player.containers = (group_drawable, group_updatable)
    Asteroid.containers = (group_drawable, group_updatable, group_asteroids)
    AsteroidField.containers = group_updatable
    Shot.containers = (group_drawable, group_updatable, group_shots)
    
    clock = pygame.time.Clock()
    dt = 0
    
    # Set the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

    player = Player(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    persistence_counter = 0
    
    # Game loop
    while game_active:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

        screen.fill(background_color)

        group_updatable.update(dt)
        
        for obj in group_drawable: 
            obj.draw(screen)

        for obj in list(group_asteroids):
            
            for shot in list(group_shots):
                if obj.is_colliding(shot):
                    obj.split()
                    shot.kill() 
 
            if obj.is_colliding(player):
                    persistence_counter += 1
        
        # This helps reduce errors from errant single frame collisions during the deletion process.
        if persistence_counter == 5:
            print("Game over!")
            game_active = False
                    
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
