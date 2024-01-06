import pygame
import time
from settings import *
import math

class Spring(pygame.sprite.Sprite):
    def __init__(self, pos, object, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load("graphics/spring.png").convert_alpha()

        self.original_image = pygame.transform.scale(self.original_image, (30, 100))
        # self.original_image = pygame.transform.rotate(self.original_image, 30)
        self.image = self.original_image.copy()

        self.object = object

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)

    def stretch(self):
        self.rect = self.image.get_rect(center=self.pos)

        self.position = self.object.rect.top - self.rect.top
        
        self.animate_image = pygame.transform.scale(
            self.original_image, (self.image.get_width(), self.position)
        )
        self.image = self.animate_image.copy()


    def get_angle(self, dot, block):
        dot_position = dot.rect.center
        block_position = (block.rect.centerx, block.rect.top)

        delta_x = block_position[0]-dot_position[0]
        delta_y = block_position[1]-dot_position[1]
        
        radians = math.asin((delta_x)/math.sqrt(((delta_x)**2)+(delta_y)**2))
        degrees = math.degrees(radians)
        
        return degrees
    def rotate(self, dot):
        degrees = self.get_angle(dot,self.object)

    

        
        self.rect = self.image.get_rect(center=self.pos)

        self.position = self.object.rect.top - dot.rect.centery
     

        self.animate_image = pygame.transform.scale(
            self.original_image, (30, self.position)
        )
        self.image = self.animate_image.copy()

        self.rotate_image = pygame.transform.rotate(self.image, degrees)
        self.image = self.rotate_image.copy()



        self.rect = self.image.get_rect(center=self.pos)
        self.rect.centerx = dot.rect.centerx + degrees * 1.7


