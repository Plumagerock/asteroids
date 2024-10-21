import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    containers = []

    def __init__(self, x, y, rotation, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt