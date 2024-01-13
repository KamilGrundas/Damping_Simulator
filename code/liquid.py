import pygame
from settings import *


class Liquid(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface((100, 500), pygame.SRCALPHA)
        self.image.fill((250, 186, 79))

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)