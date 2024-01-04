import pygame
from settings import *


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface((6, 500), pygame.SRCALPHA)
        self.image.fill("black")

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)



    def update(self, time):
        pass