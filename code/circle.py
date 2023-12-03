import pygame
from settings import *


class Circle(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.image = pygame.Surface((128, 64), pygame.SRCALPHA)
        self.image.fill("black")

        # Draw a green circle on the image surface
        # pygame.draw.circle(self.image, (0, 255, 0), (32, 32), 32)

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.current_speed = 0
        self.speed = 0.3
        self.max_speed = 10

        self.k = 1.2

        self.change_direction = True

        self.accelerate = False
        self.up = True

    def move(self, time_speed):
        # self.pos.x += 1 * self.speed * dt
        # self.rect.centerx = self.pos.x
        # print(self.current_speed)

        time_speed = round(time_speed, 2)

        if self.up:
            self.pos.y -= self.current_speed * time_speed
        else:
            self.pos.y += self.current_speed * time_speed

        if self.accelerate:
            self.current_speed += self.speed * time_speed
            if self.current_speed > self.max_speed:
                self.accelerate = False

        else:
            self.current_speed -= self.speed * time_speed
            if self.current_speed < 0:
                self.accelerate = True
                if self.change_direction == True:
                    self.up = False
                    self.change_direction = False
                    self.max_speed = self.max_speed / round(self.k, 2)
                else:
                    self.up = True
                    self.change_direction = True
                    self.max_speed = self.max_speed / round(self.k, 2)

        # print(self.max_speed)

        self.rect.centery = int(self.pos.y)

    def update(self, time_speed):
        self.move(time_speed)
