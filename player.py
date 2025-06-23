import pygame
from shot import Shot
from constants import *
from circleshape import *

class Player(CircleShape):
    def __init__(self, x: int, y: int, radius: float):
        self.x = x
        self.y = y
        self.position = pygame.Vector2(self.x, self.y)
        self.radius = radius
        
        self.rotation = 0

        self.timer = 0.0

        if hasattr(self, "containers"):
            super().__init__(self.x, self.y, self.radius)
        else:
            super().__init__(x, y, radius)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, color='white', points=self.triangle(), width=2)

    def shoot(self, dt):
        if self.timer < 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity += forward * dt * PLAYER_SHOOT_SPEED
            print('Shoot!')

        
        