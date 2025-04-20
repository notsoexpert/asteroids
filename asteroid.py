import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        theta = random.uniform(20, 50)
        child_1_velocity = self.velocity.rotate(theta)
        child_2_velocity = self.velocity.rotate(-theta)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_1.velocity = child_1_velocity * ASTEROID_SPLIT_VELOCITY_BOOST
        child_2.velocity = child_2_velocity * ASTEROID_SPLIT_VELOCITY_BOOST