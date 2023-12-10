import pygame
from settings import *
from circle import Circle
from spring import Spring
from silencer import Silencer
from side_menu import SideMenu
from button import Button
from slider import Slider
from graph import Graph
from vibrations import damped_vibrations_max


class Level:
    def __init__(self):

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
        self.side_menu = SideMenu(
            (SCREEN_WIDTH - SIDE_MENU_WIDTH / 2, SCREEN_HEIGHT / 2), self.controls
        )
        self.start_button = Button(
            (SCREEN_WIDTH - SIDE_MENU_WIDTH / 2, 150), self.controls
        )
        self.time_speed_slider = Slider(
            SLIDER_POSITIONS[3],
            self.controls,
            f"{SPEED}: x",
            0.25,
            2,
            1,
        )
        self.suppression_level_slider = Slider(
            SLIDER_POSITIONS[1],
            self.controls,
            f"{SUPPRESION_LEVEL}: ",
            0,
            2,
            1,
        )
        self.position_slider = Slider(
            SLIDER_POSITIONS[0],
            self.controls,
            f"{START_POSITION}: ",
            -2,
            2,
            0,
        )
        self.elasticity_level_slider = Slider(
            SLIDER_POSITIONS[2],
            self.controls,
            f"{ELASTICITY_COEFFICIENT}: ",
            0,
            5000,
            2500,
        )
        # self.suppression_level_slider3 = Slider(
        #     SLIDER_POSITIONS[3],
        #     self.controls,
        #     "Suppresion level",
        #     0.25,
        #     2,
        #     1,
        # )
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
        # self.sliders.add(self.suppression_level_slider2)
        # self.sliders.add(self.suppression_level_slider3)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.graph.show_graph(self.time)
        # elif keys[pygame.K_c]:
        #     self.pause = False
        # elif keys[pygame.K_w]:
            

    def text_blit(self, fps):
        # parameters = self.font.render(
        #     f"{damped_vibrations_max(self.elasticity_level_slider.k, 1, self.suppression_level_slider.k)[0]}",
        #     True,
        #     ("black"),
        # )
        # parameters2 = self.font.render(
        #     f"{damped_vibrations_max(self.elasticity_level_slider.k, 0.1, self.suppression_level_slider.k)[1]}",
        #     True,
        #     ("black"),
        # )
        # self.display_surface.blit(parameters, (100,100))
        # self.display_surface.blit(parameters2, (100,200))
        fps_text = self.font.render(f"{fps}", True, ("black"))
        time_text = self.font.render(
            f"{TIME}: {round(self.time,2)}", True, ("black")
        )
        self.display_surface.blit(fps_text, (10, 10))
        self.display_surface.blit(time_text, (10, 700))
        for slider in self.sliders:
            value_text = self.font.render(
                f"{slider.name}{slider.k:.2f}", True, ("black")
            )
            self.display_surface.blit(value_text, (1010, slider.start_y - 35))

    def run(self, fps):
        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)
        self.controls.draw(self.display_surface)
        self.circle.n = self.suppression_level_slider.k
        self.circle.k = self.elasticity_level_slider.k

        time_speed = round(self.time_speed_slider.k, 2)

        self.controls.update()
        self.input()
        self.text_blit(fps)

        self.spring.stretch()
        if self.start_button.is_playing == False:
            self.all_sprites.update(self.time)
            self.graph.take_points(self.time)
            self.time += 0.01 * time_speed

        else:
            # start_position_rescaled = self.position_slider.k
            # start_position = self.position_slider.k
            # elasicity_level = self.elasticity_level_slider.k
            # suppresion_level = self.suppression_level_slider.k
            self.circle.rect.bottom = (self.position_slider.k - B) / A
            self.circle.start_pos_y = self.position_slider.k
            self.time = 0
            self.graph.x = []
            self.graph.y = []
        self.silencer_2.move()
        self.spring.stretch()
        if self.suppression_level_slider.k == 0:
            self.silencer_2.rect.y = -1000
