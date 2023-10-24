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
        self.speed = 1

        self.gravity = 100

        self.change = False

    def move(self,dt):

        #self.pos.x += 1 * self.speed * dt

        #self.rect.centerx = self.pos.x

        
        if self.gravity == 0:
            self.change = True

        if self.gravity == 100:
            self.change = False

        if self.change == True:
            self.gravity += 1
            self.pos.y -= self.speed * dt * self.gravity
        
        if self.change == False:
            self.gravity -= 1
            self.pos.y += self.speed * dt * self.gravity


            



        

        self.rect.centery = int(self.pos.y)


    def update(self,dt):
        self.move(dt)