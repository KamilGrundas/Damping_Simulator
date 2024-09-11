import pygame
from settings import *
from vibrations import damped_vibrations


class Circle(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface((128, 64), pygame.SRCALPHA)
        self.image.fill("black")

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)

        self.start_pos_y = 0

        self.k = 0
        self.m = 1
        self.n = 2

    def move(self, time):
        self.pos.y = damped_vibrations(self.start_pos_y, time, self.k, self.m, self.n)[
            0
        ]

        self.rect.bottom = int((self.pos.y - B) / A)

    def update(self, time):
        self.move(time)
