import pygame
from settings import *
from side_menu import SideMenu
from button import Button
from level import Level
from level_2 import Level_2


class Menu:
    def __init__(self):
        self.level = Level()
        self.level.menu = True
        self.level_2 = Level_2()
        self.level_2.menu = True
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.controls = pygame.sprite.Group()

        self.font = pygame.font.Font(None, 24)

        self.setup()

    def setup(self):
        self.damped_vibrations = Button(
            (SCREEN_WIDTH / 5, SCREEN_HEIGHT / 2),
            self.controls,
            DAMPED_VIBRATIONS_IMAGE,
            DAMPED_VIBRATIONS_IMAGE,
        )

        self.forced_vibrations = Button(
            (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
            self.controls,
            FORCED_VIBRATIONS_IMAGE,
            FORCED_VIBRATIONS_IMAGE,
        )

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_m]:
            self.level.menu = False
        elif keys[pygame.K_n]:
            self.level_2.menu = False

    def run(self, fps):
        self.input()
        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)
        self.controls.draw(self.display_surface)

        if self.damped_vibrations.is_playing == False:
            self.level.menu = False
            self.damped_vibrations.is_playing = True
        if self.forced_vibrations.is_playing == False:
            self.level_2.menu = False
            self.forced_vibrations.is_playing = True

        if not self.level.menu:
            self.level.run(fps)
        elif not self.level_2.menu:
            self.level_2.run(fps)
        else:
            self.controls.update()
