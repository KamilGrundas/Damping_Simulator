import pygame
from settings import *
from spring import Spring
from wheel import Wheel
from side_menu import SideMenu
from button import Button
from slider import Slider
from graph import Graph
from dot import Dot
from vibrations import forced_vibrations
from block_wheel import BlockWheel
from block import Block


class Level_2:
    def __init__(self):
        self.menu = False
        self.show_fps = False
        self.time = 0
        self.angular_velocity = 5

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.controls = pygame.sprite.Group()

        self.font = pygame.font.Font(None, 24)

        self.sliders = pygame.sprite.Group()

        self.setup()

        self.block_wheel.move(0.1, 0.1, 0.1, self.angular_velocity, self.time)

        self.dot.rotate(self.angular_velocity, 1)
        self.spring.rotate(self.dot)
        self.spring.rect.top = self.dot.rect.centery

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

        self.radius_slider = Slider(
            SLIDER_POSITIONS[2],
            self.controls,
            f"{RADIUS}: ",
            0.1,
            0.2,
            0.15,
        )

        self.angular_velocity_slider = Slider(
            SLIDER_POSITIONS[3],
            self.controls,
            f"{ANGULAR_VELOCITY}: ",
            0,
            5,
            0,
        )

        self.elasticity_level_slider = Slider(
            SLIDER_POSITIONS[4],
            self.controls,
            f"{ELASTICITY_COEFFICIENT}: ",
            75,
            200,
            125,
        )
        self.mass_slider = Slider(
            SLIDER_POSITIONS[5],
            self.controls,
            f"{MASS}: ",
            0.1,
            0.5,
            0.25,
        )

        self.wheel = Wheel(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2), 100),
            self.all_sprites,
            WHEEL,
        )
        self.dot = Dot(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2), 100),
            self.all_sprites,
            DOT,
        )

        self.block_wheel = BlockWheel(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2), SCREEN_HEIGHT / 2),
            self.all_sprites,
            BLOCK_WHEEL,
        )

        self.block_1 = Block(
            (self.block_wheel.rect.left - 3, SCREEN_HEIGHT / 2),
            self.all_sprites,
        )
        self.block_2 = Block(
            (self.block_wheel.rect.right + 3, SCREEN_HEIGHT / 2),
            self.all_sprites,
        )

        self.spring = Spring(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2) + 30, 0),
            self.block_wheel,
            self.all_sprites,
        )

        self.graph = Graph(self.block_wheel)

        self.sliders.add(self.time_speed_slider)
        # self.connector = Connector(
        #     (SCREEN_WIDTH / 2 - 63, 100), self.circle, self.all_sprites
        # )

        # self.graph = Graph(self.circle)

        self.sliders.add(self.mass_slider)
        self.sliders.add(self.angular_velocity_slider)
        self.sliders.add(self.elasticity_level_slider)
        self.sliders.add(self.radius_slider)

    def input(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.graph.show_graph(self.time)
        if keys[pygame.K_c]:
            self.menu = True
        elif keys[pygame.K_p]:
            self.show_fps = True
        elif keys[pygame.K_w]:
            self.graph.show_graph(self.time)

    def text_blit(self, fps):
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
        self.graph.x = []
        self.graph.y = []
        self.start_button.is_playing = True

    def run(self, fps):
        self.controls.update()
        self.input()

        if self.menu_button.is_playing == False:
            self.menu = True
            self.menu_button.is_playing = True

        self.angular_velocity = self.angular_velocity_slider.k
        m = self.mass_slider.k
        k = self.elasticity_level_slider.k
        r = self.radius_slider.k
        r_scaled = int((r - 0.1) * ((28.6 - 7.125) / (0.4 - 0.1)) + 7.125)
        self.dot.radius = (r - 0.1) * ((50 - 7.125) / (0.4 - 0.1)) + 7.125
        self.wheel.scale(r_scaled)

        time_speed = self.time_speed_slider.k

        if self.replay_button.is_playing == False:
            self.reset()
            self.replay_button.is_playing = True

        if self.start_button.is_playing == False:
            # self.graph.take_points(self.time)
            self.time += 0.01 * time_speed
            self.block_wheel.move(m, self.angular_velocity, r, k, self.time)
            self.spring.rotate(self.dot)
            self.spring.rect.top = self.dot.rect.centery
            self.dot.rotate(self.angular_velocity, time_speed)
            self.graph.take_points(self.time)

        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)

        self.controls.draw(self.display_surface)

        self.text_blit(fps)
        # self.spring.stretch()
