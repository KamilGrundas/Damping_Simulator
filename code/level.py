import pygame
from settings import *
from circle import Circle
from spring import Spring
from silencer import Silencer
from side_menu import SideMenu
from button import Button
from slider import Slider
from graph import Graph
from vibrations import damped_vibrations_max, damped_vibrations


class Level:
    def __init__(self):
        self.menu = False
        self.show_fps = False
        self.time = 0

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.controls = pygame.sprite.Group()

        self.font = pygame.font.Font(None, 24)

        self.sliders = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.menu_button = Button((50, 50), self.controls, MENU_BUTTON, MENU_BUTTON)
        self.side_menu = SideMenu(
            (SCREEN_WIDTH - SIDE_MENU_WIDTH / 2, SCREEN_HEIGHT / 2), self.controls
        )
        self.start_button = Button(
            (SCREEN_WIDTH - SIDE_MENU_WIDTH / 2 - 70, 75),
            self.controls,
            PAUSE_BUTTON,
            PLAY_BUTTON,
        )
        self.replay_button = Button(
            (SCREEN_WIDTH - SIDE_MENU_WIDTH / 2 + 70, 75),
            self.controls,
            REPLAY_BUTTON_1,
            REPLAY_BUTTON_1,
        )
        self.time_speed_slider = Slider(
            SLIDER_POSITIONS[0],
            self.controls,
            f"{SPEED}: x",
            0.05,
            2,
            1,
        )
        self.suppression_level_slider = Slider(
            SLIDER_POSITIONS[3],
            self.controls,
            f"{SUPPRESION_LEVEL}: ",
            0,
            10,
            5,
        )
        self.position_slider = Slider(
            SLIDER_POSITIONS[2],
            self.controls,
            f"{START_POSITION}: ",
            -2,
            2,
            0,
        )
        self.elasticity_level_slider = Slider(
            SLIDER_POSITIONS[4],
            self.controls,
            f"{ELASTICITY_COEFFICIENT}: ",
            0,
            5000,
            2500,
        )
        self.mass_slider = Slider(
            SLIDER_POSITIONS[5],
            self.controls,
            f"{MASS}: ",
            0.1,
            2,
            1,
        )
        self.circle = Circle(
            ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2, SCREEN_HEIGHT / 2), self.all_sprites
        )
        self.spring = Spring(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2) + 30, 0),
            self.circle,
            self.all_sprites,
        )
        self.silencer = Silencer(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2) - 30, 0),
            self.circle,
            self.all_sprites,
            SILENCER_1,
        )
        self.silencer_2 = Silencer(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2) - 30, 0),
            self.circle,
            self.all_sprites,
            SILENCER_2,
        )
        # self.connector = Connector(
        #     (SCREEN_WIDTH / 2 - 63, 100), self.circle, self.all_sprites
        # )

        self.graph = Graph(self.circle)

        self.sliders.add(self.time_speed_slider)
        self.sliders.add(self.suppression_level_slider)
        self.sliders.add(self.position_slider)
        self.sliders.add(self.elasticity_level_slider)
        self.sliders.add(self.mass_slider)
        # self.sliders.add(self.suppression_level_slider3)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.graph.show_graph(self.time)
        elif keys[pygame.K_c]:
            self.menu = True
        elif keys[pygame.K_p]:
            self.show_fps = True

    def text_blit(self, fps):
        parameters = self.font.render(
            f"Wsp. tłumienia (h): {round(damped_vibrations_max(self.elasticity_level_slider.k, self.mass_slider.k, self.suppression_level_slider.k)[0],2)}",
            True,
            ("black"),
        )
        parameters2 = self.font.render(
            f"Kryt. wsp. tłumienia (hk): {round(damped_vibrations_max(self.elasticity_level_slider.k, self.mass_slider.k, self.suppression_level_slider.k)[1],2)}",
            True,
            ("black"),
        )
        parameters3 = self.font.render(
            f"ω: {round(damped_vibrations(self.position_slider.k,self.time,self.elasticity_level_slider.k,self.mass_slider.k,self.suppression_level_slider.k)[1],2)}",
            True,
            ("black"),
        )
        parameters4 = self.font.render(
            f"ωt: {round(damped_vibrations(self.position_slider.k,self.time,self.elasticity_level_slider.k,self.mass_slider.k,self.suppression_level_slider.k)[2],2)}",
            True,
            ("black"),
        )
        self.display_surface.blit(parameters, (1010, 225))
        self.display_surface.blit(parameters2, (1010, 250))
        self.display_surface.blit(parameters3, (1010, 275))
        self.display_surface.blit(parameters4, (1010, 300))
        fps_text = self.font.render(f"{fps}", True, ("black"))
        time_text = self.font.render(f"{TIME}: {round(self.time,2)}", True, ("black"))
        if self.show_fps == True:
            self.display_surface.blit(fps_text, (10, 10))
        self.display_surface.blit(time_text, (10, 700))
        for slider in self.sliders:
            value_text = self.font.render(
                f"{slider.name}{slider.k:.2f}", True, ("black")
            )
            self.display_surface.blit(value_text, (1010, slider.start_y - 35))

    def reset(self):
        self.time = 0
        self.graph.clear_points()
        self.start_button.is_playing = True

    def run(self, fps):
        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)
        self.controls.draw(self.display_surface)
        self.circle.n = self.suppression_level_slider.k
        self.circle.k = self.elasticity_level_slider.k
        self.circle.m = self.mass_slider.k

        time_speed = round(self.time_speed_slider.k, 2)

        self.controls.update()
        self.input()
        self.text_blit(fps)

        self.spring.stretch(True)
        if self.start_button.is_playing == False:
            self.all_sprites.update(self.time)
            self.graph.take_points(self.time)
            self.time += 0.01 * time_speed

        elif self.time == 0:
            self.circle.rect.bottom = (self.position_slider.k - B) / A
            self.circle.start_pos_y = self.position_slider.k
            self.replay_button.is_playing = True

        if self.replay_button.is_playing == False:
            self.reset()

        if self.menu_button.is_playing == False:
            self.reset()
            self.menu = True
            self.menu_button.is_playing = True

        self.silencer_2.move()
        self.spring.stretch(True)
        if self.suppression_level_slider.k == 0:
            self.silencer_2.rect.y = -1000
            self.silencer.rect.y = -1000
            self.spring.rect.centerx = (SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2
        else:
            self.silencer.rect.y = 0
            self.spring.rect.centerx = ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2) + 30
