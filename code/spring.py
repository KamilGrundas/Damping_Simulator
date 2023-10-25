import pygame
from settings import *


class Spring(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.image.load("graphics/spring.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (200,50))
    

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100



    def move(self,dt):

    #     self.s += 10 * dt
    #     if self.s > 300:
    #         self.image = pygame.transform.scale(self.image, (200,50))


    #     self.image = pygame.transform.scale(self.image,(self.s, 50))

        self.pos.x += 1 * self.speed * dt

        self.rect.centerx = self.pos.x

        
        # if self.gravity == 0:
        #     self.change = True

        # if self.gravity == 100:
        #     self.change = False

        # if self.change == True:
        #     self.gravity += 1
        #     self.pos.y -= self.speed * dt * self.gravity
        
        # if self.change == False:
        #     self.gravity -= 1
        #     self.pos.y += self.speed * dt * self.gravity

    def update(self,dt):
        self.move(dt)