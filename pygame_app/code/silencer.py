import pygame
from settings import *
from matplotlib import pyplot as plt


class Silencer(pygame.sprite.Sprite):
    def __init__(self, pos, circle, group, png):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load(png).convert_alpha()
        self.image = self.original_image.copy()

        self.circle = circle

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

        self.rect.top = self.pos.y

    def move(self):
        self.rect.bottom = self.circle.rect.top

    def rotate(self):

        self.rotate_image = pygame.transform.rotate(self.original_image, 180)
        self.image = self.rotate_image.copy()

    def scale(self):
        self.scale_image = pygame.transform.scale(
            self.image, (self.image.get_width(), 250)
        )
        self.image = self.scale_image.copy()
