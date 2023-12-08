import pygame
import time
from settings import *
from matplotlib import pyplot as plt


class Spring(pygame.sprite.Sprite):
    def __init__(self, pos, circle, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load("graphics/spring.png").convert_alpha()
        self.original_image = pygame.transform.rotate(self.original_image, 90)
        self.original_image = pygame.transform.scale(self.original_image, (30, 100))
        self.image = self.original_image.copy()

        self.circle = circle

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

    def stretch(self):
        self.rect = self.image.get_rect(center=self.pos)
        self.rect.top = self.pos.y

        self.position = self.circle.rect.top - self.rect.top

        self.animate_image = pygame.transform.scale(
            self.original_image, (self.image.get_width(), self.position)
        )
        self.image = self.animate_image.copy()
