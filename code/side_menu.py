import pygame
from settings import *

class SideMenu(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)


        self.image = pygame.Surface((SIDE_MENU_WIDTH, SCREEN_HEIGHT))
        self.image.fill("grey")
        self.rect = self.image.get_rect(center=pos)
        
