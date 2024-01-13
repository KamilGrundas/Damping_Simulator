import pygame
from settings import *



class DynamicBlock(pygame.sprite.Sprite):
    def __init__(self, pos, group, size):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill("black")

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

    def move(self, m, w, r, k, time):
        # self.pos.y = forced_vibrations(w, time)
        self.pos.y = 0

        self.rect.bottom = int((self.pos.y + 2) * ((720 - 285) / (2 + 2)) + 285)