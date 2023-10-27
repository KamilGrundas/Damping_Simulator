# import pygame
# from settings import *

# class Spring(pygame.sprite.Sprite):

#     def __init__(self, pos, group):
#         super().__init__(group)

#         # Create an image surface with a transparent background
#         self.original_image = pygame.image.load("graphics/spring.png").convert_alpha()
#         self.original_image = pygame.transform.scale(self.original_image, (30, 70))
#         self.image = self.original_image.copy()

#         # Set the position of the sprite
#         self.rect = self.image.get_rect(center=pos)

#         self.pos = pygame.math.Vector2(self.rect.center)
#         self.speed = 100
#         self.expanding = True

#         self.max_width = 30
#         self.min_width = 10
#         self.max_height = 400
#         self.min_height = 70
#         self.stretch_speed = 1
#         self.stretch_speed_y = 5

#     def update(self, dt):
#         self.stretch(dt)

#     def stretch(self, dt):
        


#         self.rect = self.image.get_rect(center=self.pos)
#         self.rect.top = self.pos.y

#         if self.expanding:
#             self.image = pygame.transform.scale(self.image, (self.image.get_width() + self.stretch_speed, self.image.get_height() - self.stretch_speed_y))

#             if self.image.get_width() >= self.max_width or self.image.get_height() <= self.min_height:
#                 self.expanding = False
#         else:
#             self.image = pygame.transform.scale(self.image, (self.image.get_width() - self.stretch_speed, self.image.get_height() + self.stretch_speed_y))

#             if self.image.get_width() <= self.min_width or self.image.get_height() >= self.max_height:
#                 self.expanding = True


                
import pygame
from settings import *

class Spring(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load("graphics/spring.png").convert_alpha()
        self.original_image = pygame.transform.rotate(self.original_image, 90)
        self.original_image = pygame.transform.scale(self.original_image, (30, 100))
        self.image = self.original_image.copy()

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100
        self.expanding = True

        self.max_width = 30
        self.min_width = 10
        self.max_height = 400
        self.min_height = 70
        self.stretch_speed = 1
        self.stretch_speed_y = 5

    def update(self, dt):
        self.stretch(dt)

    def stretch(self, dt):
        


        self.rect = self.image.get_rect(center=self.pos)
        self.rect.top = self.pos.y

        if self.expanding:

            self.animate_image = pygame.transform.scale(self.original_image, (self.image.get_width() + self.stretch_speed, self.image.get_height() - self.stretch_speed_y))
            self.image = self.animate_image.copy()

            if self.image.get_width() >= self.max_width or self.image.get_height() <= self.min_height:
                self.expanding = False
        else:

            self.animate_image = pygame.transform.scale(self.original_image, (self.image.get_width() - self.stretch_speed, self.image.get_height() + self.stretch_speed_y))
            self.image = self.animate_image.copy()


            if self.image.get_width() <= self.min_width or self.image.get_height() >= self.max_height:
                self.expanding = True

