import pygame
from settings import *
from circle import Circle
from spring import Spring
from silencer import Silencer
from connector import Connector
from side_menu import SideMenu
from button import Button
from slider import Slider
from graph import Graph


class Level:
    def __init__(self):
        self.pause = False

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
            "Playback speed: x",
            0.25,
            2,
            1,
        )
        self.suppression_level_slider = Slider(
            SLIDER_POSITIONS[1],
            self.controls,
            "Suppresion level: ",
            0.25,
            2,
            1,
        )
        self.position_slider = Slider(
            SLIDER_POSITIONS[0],
            self.controls,
            "Start position: ",
            -2,
            2,
            0,
        )
        # self.suppression_level_slider2 = Slider(
        #     SLIDER_POSITIONS[2],
        #     self.controls,
        #     "Suppresion level",
        #     0.25,
        #     2,
        #     1,
        # )
        # self.suppression_level_slider3 = Slider(
        #     SLIDER_POSITIONS[3],
        #     self.controls,
        #     "Suppresion level",
        #     0.25,
        #     2,
        #     1,
        # )
        self.circle = Circle(((SCREEN_WIDTH - SIDE_MENU_WIDTH) / 2, SCREEN_HEIGHT/2), self.all_sprites)
        # self.spring = Spring((SCREEN_WIDTH / 2, 10), self.circle, self.all_sprites)
        # self.silencer = Silencer(
        #     (SCREEN_WIDTH / 2 - 64, 100), self.circle, self.all_sprites
        # )
        # self.connector = Connector(
        #     (SCREEN_WIDTH / 2 - 63, 100), self.circle, self.all_sprites
        # )

        self.graph = Graph(self.circle)
        print(self.graph.object.rect.centery)

        self.sliders.add(self.time_speed_slider)
        self.sliders.add(self.suppression_level_slider)
        self.sliders.add(self.position_slider)
        # self.sliders.add(self.suppression_level_slider2)
        # self.sliders.add(self.suppression_level_slider3)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            self.pause = True
        elif keys[pygame.K_c]:
            self.pause = False
            self.spring.show_graph = False
        elif keys[pygame.K_w]:
            self.spring.show_graph = True

    def text_blit(self, fps):
        fps_text = self.font.render(f"{fps}", True, ("black"))
        self.display_surface.blit(fps_text, (10, 10))
        for slider in self.sliders:
            value_text = self.font.render(
                f"{slider.name}{slider.k:.2f}", True, ("black")
            )
            self.display_surface.blit(value_text, (1010, slider.start_y - 35))



    def run(self, fps):

        self.display_surface.fill("white")
        self.all_sprites.draw(self.display_surface)
        self.controls.draw(self.display_surface)
        # self.circle.k = self.suppression_level_slider.k
        time_speed = self.time_speed_slider.k 
        
        self.controls.update()
        self.input()
        self.text_blit(fps)
        if self.start_button.is_playing == False:
            self.all_sprites.update(time_speed)
        else:
            self.circle.rect.bottom = (self.position_slider.k - B) / A
            self.circle.start_pos_y = self.position_slider.k
