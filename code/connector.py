import pygame
import time
from settings import *
from matplotlib import pyplot as plt

class Connector(pygame.sprite.Sprite):

    def __init__(self, pos, circle, group):
        super().__init__(group)

        # Create an image surface with a transparent background
        self.original_image = pygame.image.load("graphics/connector.png").convert_alpha()
        self.original_image = pygame.transform.rotate(self.original_image, 90)
        self.original_image = pygame.transform.scale(self.original_image, (5, 100))
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


    def update(self):
        if self.show_graph == False:
            self.stretch()
        else:
            plt.rcParams["figure.figsize"] = [7.00, 3.50]
            plt.rcParams["figure.autolayout"] = True
            plt.xlim(0, 15)
            plt.ylim(100, 700)
            plt.grid()
            plt.plot(self.x, self.y, marker="o", markersize=2, markeredgecolor="red", markerfacecolor="green")
            plt.show()

    def stretch(self):

        
        self.time = time.time() - self.start_time

        self.rect = self.image.get_rect(center=self.pos)
        self.rect.top = self.pos.y


        self.x.append(self.time)
        # Use a sine wave to calculate the vertical position
        self.y.append(self.rect.bottom)
        #print(self.circle.rect.top)
        
        self.position = (self.circle.rect.top - self.rect.top)

        self.animate_image = pygame.transform.scale(self.original_image, (self.image.get_width(), self.position))
        self.image = self.animate_image.copy()