import pygame
from settings import *
from matplotlib import pyplot as plt
import pygame.gfxdraw

# draw.circle is not anti-aliased and looks rather ugly.
# pygame.draw.circle(ATOM_IMG, (0, 255, 0), (15, 15), 15)
# gfxdraw.aacircle looks a bit better.


class Wheel(pygame.sprite.Sprite):
    def __init__(self, pos, group, png):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)

    def scale(self, radius):
        diameter = radius * 2
        self.image.fill("white")

        pygame.gfxdraw.filled_circle(self.image, 30, 30, int(diameter), (100, 100, 100))
        # pygame.gfxdraw.aacircle(self.image, 30, 30, int(diameter), (0, 0, 0))
        # self.scaled_image = pygame.transform.scale(self.original_image, (diameter,diameter))
