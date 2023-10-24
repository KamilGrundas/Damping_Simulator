import pygame
from settings import *


class Circle(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface((64, 64), pygame.SRCALPHA)
        
        # Draw a green circle on the image surface
        pygame.draw.circle(self.image, (0, 255, 0), (32, 32), 32)

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100

    def move(self,dt):

        self.pos.x += 1 * self.speed * dt

        self.rect.centerx = self.pos.x

        self.pos.y += 1 * self.speed * dt

        self.rect.centery = self.pos.y


    def update(self,dt):
        self.move(dt)