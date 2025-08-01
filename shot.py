import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x: int, y: int, radius: float):
        self.x = x
        self.y = y
        self.position = pygame.Vector2(self.x, self.y)
        self.radius = radius

        if hasattr(self, "containers"):
            super().__init__(self.x, self.y, self.radius)
        else:
            super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color='green', center=self.position, radius=SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
