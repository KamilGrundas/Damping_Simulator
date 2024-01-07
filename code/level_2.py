import pygame
from settings import *
from circle import Circle
from spring import Spring
from silencer import Silencer
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
        self.angular_velocity = 2

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.controls = pygame.sprite.Group()

        self.font = pygame.font.Font(None, 24)

        self.sliders = pygame.sprite.Group()

        self.setup()

        self.block_wheel.move(self.time)

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

        self.sliders.add(self.time_speed_slider)
        # self.connector = Connector(
        #     (SCREEN_WIDTH / 2 - 63, 100), self.circle, self.all_sprites
        # )

        # self.graph = Graph(self.circle)

        # self.sliders.add(self.suppression_level_slider3)

    def input(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.graph.show_graph(self.time)
        if keys[pygame.K_c]:
            self.menu = True
        elif keys[pygame.K_p]:
            self.show_fps = True

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

    def run(self, fps):
        self.controls.update()
        if self.menu_button.is_playing == False:
            self.menu = True
            self.menu_button.is_playing = True

        time_speed = self.time_speed_slider.k

        if self.start_button.is_playing == False:
            # self.graph.take_points(self.time)
            self.time += 0.01 * time_speed
            self.block_wheel.move(self.time)
            self.spring.rotate(self.dot)
            self.spring.rect.top = self.dot.rect.centery
            self.dot.rotate(self.angular_velocity, time_speed)

        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)

        self.controls.draw(self.display_surface)

        self.text_blit(fps)
        # self.spring.stretch()
