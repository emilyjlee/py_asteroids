import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    containers = None
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        for container in self.__class__.containers:
            container.add(self)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    def update(self, dt):
        self.position += (self.velocity * dt)
