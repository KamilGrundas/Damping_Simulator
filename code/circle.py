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
        self.time = 0
        self.k = 4200
        self.m = 2
        self.b = 2

    def move(self, time_speed):
        time_speed = round(time_speed, 2)
        self.time += 0.01 * time_speed

        self.pos.y = damped_vibrations(
            self.start_pos_y, self.time, self.k, self.m, self.b
        )

        self.rect.bottom = int((self.pos.y - B) / A)

    def update(self, time_speed):
        self.move(time_speed)
