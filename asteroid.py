import random
import pygame
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    containers = []

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(10, 50)
        new_rotate_1 = self.velocity.rotate(new_angle)
        new_rotate_2 = self.velocity.rotate(-new_angle)
        new_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_1.velocity = new_rotate_1 * 1.2
        new_2.velocity = new_rotate_2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt