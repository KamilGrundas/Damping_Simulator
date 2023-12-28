import pygame
from settings import *
from side_menu import SideMenu
from button import Button
from level import Level


class Menu:
    def __init__(self):

        

        self.level = Level()
        self.level.menu = True
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.controls = pygame.sprite.Group()

        self.font = pygame.font.Font(None, 24)

        self.setup()

    def setup(self):
        self.side_menu = SideMenu(
            (SCREEN_WIDTH - SIDE_MENU_WIDTH / 2, SCREEN_HEIGHT / 2), self.controls
        )
        self.start_button = Button(
            (SCREEN_WIDTH - SIDE_MENU_WIDTH / 2, 150), self.controls, PAUSE_BUTTON, PLAY_BUTTON
        )


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_m]:
            self.level.menu = False



    def run(self, fps):
        self.input()
        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)
        self.controls.draw(self.display_surface)


        self.controls.update()
        if self.level.menu == False:
            self.level.run(fps)

