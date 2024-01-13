import pygame
from settings import *
from spring import Spring
from side_menu import SideMenu
from button import Button
from slider import Slider
from graph import Graph
from dynamic_block import DynamicBlock
from vibrations_c import Solution




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

        self.sliders = pygame.sprite.Group()

        self.setup()

        self.spring.rect.top = 0
        self.spring_2.pos.y = self.block.rect.bottom
        self.spring.stretch()
        self.spring_2.stretch()

        self.solution = Solution()

        self.solution.generate_solution()

        

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

        self.block = DynamicBlock(
            ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2, SCREEN_HEIGHT / 2.5),
            self.all_sprites, (150, 100)
        )

        self.dynamic_dumper = DynamicBlock(
            ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2, (SCREEN_HEIGHT / 2) + 100),
            self.all_sprites, (25,25)
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
        self.graph.clear_points()
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

        time_speed = self.time_speed_slider.k

        if self.replay_button.is_playing == False:
            self.reset()
            self.replay_button.is_playing = True

        if self.start_button.is_playing == False:
            # self.graph.take_points(self.time)
            self.time += 0.01 * time_speed
            self.spring.stretch()
            self.spring_2.stretch()
            self.spring.rect.top = 0
            self.spring_2.pos.y = self.block.rect.bottom
            self.graph.take_points(self.time)
            self.block.rect.centery = int((self.solution.read_y(self.time)[0] + 2) * ((480 - 285) / (2 + 2)) + 285)
            self.dynamic_dumper.rect.centery = int((self.solution.read_y(self.time)[1] + 2) * ((600 - 500) / (2 + 2)) + 600)

        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)

        self.controls.draw(self.display_surface)

        self.text_blit(fps)

        # self.spring.stretch()
