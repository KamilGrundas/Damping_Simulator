import pygame
import time
from settings import *
from matplotlib import pyplot as plt

class Silencer(pygame.sprite.Sprite):

    def __init__(self, pos, circle, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load("graphics/silencer.png").convert_alpha()
        self.image = self.original_image.copy()

        self.circle = circle

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100
        self.expanding = True

        self.max_width = 30
        self.min_width = 10
        self.max_height = 300
        self.min_height = 70
        self.stretch_speed = 100
        self.stretch_speed_y = 400

        self.show_graph = False

        self.medium = (self.max_height + self.min_height) /2

        self.start_time = time.time()
        self.x = []
        self.y = []
        self.time = 0




