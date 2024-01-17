import pygame
from settings import *
from spring import Spring
from side_menu import SideMenu
from button import Button
from slider import Slider
from graph import Graph
from vibrations import forced_vibrations
from dynamic_block import DynamicBlock
from block import Block
from silencer import Silencer


class Level_2:
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

        self.silencer.rotate()
        self.silencer_2.rotate()
        self.silencer.scale()
        self.silencer_2.scale()

        self.spring.rect.top = self.dynamic_block.rect.bottom


        self.spring.stretch(False)


        self.silencer_2.rect.top = self.dynamic_block.rect.bottom

    def setup(self):

        self.menu_button = Button((50, 50), self.controls, MENU_BUTTON, MENU_BUTTON)

        self.graph = Button((700, 500), self.controls, GRAPH, GRAPH)

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



        self.damp_slider = Slider(
            SLIDER_POSITIONS[2],
            self.controls,
            f"{SUPPRESION_LEVEL} (h): ",
            0,
            20,
            10,
        )

        self.angular_velocity_slider = Slider(
            SLIDER_POSITIONS[3],
            self.controls,
            f"{FREQUENCY} (p): ",
            0,
            50,
            25,
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
            1,
            5,
            3,
        )



        self.block = Block(
            ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 3, 680),
            self.all_sprites,
        )

        self.dynamic_block = DynamicBlock(
            ((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 3, SCREEN_HEIGHT / 3),
            self.all_sprites,
            (150, 100),
        )

        self.spring = Spring(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 3) + 30, 680),
            self.dynamic_block,
            self.all_sprites,
        )

        self.silencer = Silencer(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 3) - 30,430),
            self.dynamic_block,
            self.all_sprites,
            SILENCER_1,
        )
        self.silencer_2 = Silencer(
            (((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 3) - 30, SCREEN_HEIGHT / 2.5 + 50),
            self.dynamic_block,
            self.all_sprites,
            SILENCER_2,
        )

        self.graph = Graph(self.dynamic_block)

        self.sliders.add(self.time_speed_slider)
        # self.connector = Connector(
        #     (SCREEN_WIDTH / 2 - 63, 100), self.circle, self.all_sprites
        # )

        # self.graph = Graph(self.circle)

        self.sliders.add(self.mass_slider)
        self.sliders.add(self.angular_velocity_slider)
        self.sliders.add(self.elasticity_level_slider)
        self.sliders.add(self.damp_slider)

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
        p = self.angular_velocity_slider.k
        h = self.damp_slider.k
        m = self.mass_slider.k
        k = self.elasticity_level_slider.k
        parameters = self.font.render(
            f"p/w:{round(forced_vibrations(m,k,h,p,self.time)[1],2)}",
            True,
            ("black"),
        )
        self.display_surface.blit(parameters, (1010, 225))
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


        p = self.angular_velocity_slider.k
        h = self.damp_slider.k
        m = self.mass_slider.k
        k = self.elasticity_level_slider.k


        time_speed = self.time_speed_slider.k

        if self.replay_button.is_playing == False:
            self.reset()
            self.replay_button.is_playing = True

        if self.start_button.is_playing == False:
            # self.graph.take_points(self.time)
            self.time += 0.01 * time_speed
            self.graph.take_points(self.time)
            self.dynamic_block.move_2(forced_vibrations(m,k,h,p,self.time)[0])

        
        self.silencer_2.rect.top = self.dynamic_block.rect.bottom
        self.spring.stretch(False)
        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)


        self.controls.draw(self.display_surface)

        self.text_blit(fps)
        # self.spring.stretch()
