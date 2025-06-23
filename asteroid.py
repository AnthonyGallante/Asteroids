import pygame
import random

from constants import *
from circleshape import *

class Asteroid(CircleShape):
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
        pygame.draw.circle(screen, color='white', center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            deflection_angle = random.uniform(
                ASTEROID_MIN_DEFLECTION_ANGLE, 
                ASTEROID_MAX_DEFLECTION_ANGLE)
            
            v1 = self.velocity.rotate(deflection_angle) * random.uniform(1.0, 1.25)
            v2 = self.velocity.rotate(-deflection_angle) * random.uniform(1.0, 1.25)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid1.velocity, new_asteroid2.velocity = v1, v2

