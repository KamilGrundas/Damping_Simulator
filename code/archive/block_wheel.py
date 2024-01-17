import pygame
from settings import *
from vibrations import forced_vibrations


class BlockWheel(pygame.sprite.Sprite):
    def __init__(self, pos, group, png):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load(png).convert_alpha()
        self.image = self.original_image.copy()

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

    def move(self, m, w, r, k, time):
        # self.pos.y = forced_vibrations(w, time)
        self.pos.y = forced_vibrations(m, w, r, k, time)

        self.rect.bottom = int((self.pos.y + 2) * ((720 - 285) / (2 + 2)) + 285)
