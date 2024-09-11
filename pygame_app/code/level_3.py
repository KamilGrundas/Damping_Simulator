import pygame
from settings import *
from spring import Spring
from side_menu import SideMenu
from button import Button
from slider import Slider
from graph import Graph
from dynamic_block import DynamicBlock
from vibrations import dynamic_dumping


class Level_3:
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
        self.font_40 = pygame.font.Font(None, 40)

        self.sliders = pygame.sprite.Group()

        self.setup()

        self.spring.rect.top = 0
        self.spring_2.pos.y = self.block.rect.bottom
        self.spring.stretch(True)
        self.spring_2.stretch(True)

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

        self.mass_1_slider = Slider(
            SLIDER_POSITIONS[2],
            self.controls,
            f"{MASS} (m1): ",
            45,
            100,
            70,
        )

        self.elasticity_level_1_slider = Slider(
            SLIDER_POSITIONS[3],
            self.controls,
            f"{ELASTICITY_COEFFICIENT} (k1): ",
            500,
            2500,
            1500,
        )

        self.elasticity_level_2_slider = Slider(
            SLIDER_POSITIONS[5],
            self.controls,
            f"{ELASTICITY_COEFFICIENT} (k2): ",
            25,
            225,
            120,
        )
        self.mass_2_slider = Slider(
            SLIDER_POSITIONS[4],
            self.controls,
            f"{MASS} tłumika (m2): ",
            0.5,
            4.5,
            2,
        )

        self.block = DynamicBlock(
            ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2, SCREEN_HEIGHT / 2.5),
            self.all_sprites,
            (150, 100),
        )

        self.dynamic_dumper = DynamicBlock(
            ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2, (SCREEN_HEIGHT / 2) + 100),
            self.all_sprites,
            (25, 25),
        )

        self.spring = Spring(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2), 0),
            self.block,
            self.all_sprites,
        )

        self.spring_2 = Spring(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2), 0),
            self.dynamic_dumper,
            self.all_sprites,
        )

        self.graph = Graph(self.block)

        self.sliders.add(self.time_speed_slider)
        self.sliders.add(self.elasticity_level_1_slider)
        self.sliders.add(self.mass_1_slider)
        self.sliders.add(self.elasticity_level_2_slider)
        self.sliders.add(self.mass_2_slider)
    def input(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.graph.show_graph(self.time)
        if keys[pygame.K_c]:
            self.menu = True
        elif keys[pygame.K_p]:
            self.show_fps = True
        elif keys[pygame.K_w]:
            self.graph.show_graph(self.time / 25)

    def text_blit(self, fps):
        parameters = self.font.render(
            f"{OPTIMAL_ELASCITY} (k2):{round(dynamic_dumping(self.mass_1_slider.k, self.elasticity_level_1_slider.k, self.mass_2_slider.k, self.elasticity_level_2_slider.k, self.time)[2],2)}",
            True,
            ("black"),
        )
        parameters2 = self.font_40.render(
            "m1",
            True,
            ("white"),
        )
        parameters3 = self.font_40.render(
            "k1",
            True,
            ("black"),
        )

        self.display_surface.blit(parameters, (1010, 225))
        self.display_surface.blit(parameters2, (self.block.rect.centerx - 20, self.block.rect.centery - 15))
        self.display_surface.blit(parameters3, (self.spring.rect.centerx + 20, self.spring.rect.centery))

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
        self.controls.update()
        self.input()


        m1 = self.mass_1_slider.k
        k1 = self.elasticity_level_1_slider.k
        m2 = self.mass_2_slider.k
        k2 = self.elasticity_level_2_slider.k

        if self.menu_button.is_playing == False:
            self.menu = True
            self.menu_button.is_playing = True

        time_speed = self.time_speed_slider.k

        if self.replay_button.is_playing == False:
            self.reset()
            self.replay_button.is_playing = True

        if self.start_button.is_playing == False:
            self.time += 0.01 * time_speed

            self.block.move(dynamic_dumping(m1,k1,m2, k2, self.time)[0])
            self.dynamic_dumper.rect.centery = (
                int(
                    (dynamic_dumping(m1,k1,m2, k2, self.time)[1] + 1)
                    * ((480 - 285) / (1 + 1))
                    + 285
                )
                + 250
            )

            self.graph.take_points(self.time / 25)
            self.spring.stretch(True)
            self.spring_2.stretch(True)
            self.spring.rect.top = 0
            self.spring_2.pos.y = self.block.rect.bottom - 3

        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)

        self.controls.draw(self.display_surface)

        self.text_blit(fps)

        # self.spring.stretch()
