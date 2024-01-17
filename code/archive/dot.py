import pygame
from settings import *


class Dot(pygame.sprite.Sprite):
    def __init__(self, pos, group, png):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load(png).convert_alpha()
        self.image = self.original_image.copy()

        # Center point
        self.center_point = pos

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.radius = 15
        self.angle = 90  # Początkowy kąt obiektu na okręgu

    def rotate(self, angular_velocity, time_speed):
        # Oblicz nowy kąt obiektu na okręgu
        self.angle += angular_velocity * time_speed

        # Oblicz nową pozycję na okręgu przy użyciu współrzędnych biegunowych
        x = self.radius * pygame.math.Vector2(1, 0).rotate(self.angle).x
        y = self.radius * pygame.math.Vector2(1, 0).rotate(self.angle).y

        # Ustaw nową pozycję obiektu względem center_point
        self.pos = self.center_point + pygame.math.Vector2(x, y)
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def update(self, angular_velocity):
        self.rotate(angular_velocity)
