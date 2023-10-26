# import pygame
# from settings import *


# class Spring(pygame.sprite.Sprite):

#     def __init__(self, pos, group):
#         super().__init__(group)

#         # Create an image surface with a transparent background
#         self.image = pygame.image.load("graphics/spring.png").convert_alpha()

#         self.image = pygame.transform.scale(self.image, (200,50))
    

#         # Set the position of the sprite
#         self.rect = self.image.get_rect(center=pos)

#         self.pos = pygame.math.Vector2(self.rect.center)
#         self.speed = 100



#     def move(self,dt):

#     #     self.s += 10 * dt
#     #     if self.s > 300:
#     #         self.image = pygame.transform.scale(self.image, (200,50))


#     #     self.image = pygame.transform.scale(self.image,(self.s, 50))

#         self.pos.x += 1 * self.speed * dt

#         self.rect.centerx = self.pos.x

        
#         # if self.gravity == 0:
#         #     self.change = True

#         # if self.gravity == 100:
#         #     self.change = False

#         # if self.change == True:
#         #     self.gravity += 1
#         #     self.pos.y -= self.speed * dt * self.gravity
        
#         # if self.change == False:
#         #     self.gravity -= 1
#         #     self.pos.y += self.speed * dt * self.gravity

#     def update(self,dt):
#         self.move(dt)


import pygame
from settings import *

class Spring(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load("graphics/spring.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (200, 100))
        self.image = self.original_image.copy()

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100
        self.expanding = True
        self.expanding_h = True
        self.max_width = 400
        self.min_width = 200
        self.max_height = 200
        self.min_height = 100
        self.stretch_speed = 5
        self.stretch_speed_y = 1

    def update(self, dt):
        self.stretch(dt)

    def stretch(self, dt):
        



        if self.expanding:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() + self.stretch_speed, self.image.get_height()))
            self.pos.x += self.image.get_width() * dt
            if self.image.get_width() >= self.max_width:
                self.expanding = False
        else:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() - self.stretch_speed, self.image.get_height()))
            self.pos.x -= self.image.get_width() * dt
            if self.image.get_width() <= self.min_width:
                self.expanding = True

        if self.expanding:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() , self.image.get_height() - self.stretch_speed_y))
            if self.image.get_height() >= self.max_height:
                self.expanding_h = False
        else:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() , self.image.get_height() + self.stretch_speed_y))
            if self.image.get_height() <= self.min_height:
                self.expanding_h = True

        
        self.rect = self.image.get_rect(center=self.pos)

        # Handle boundary conditions if needed
