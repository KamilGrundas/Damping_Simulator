import pygame
from settings import *


class Slider(pygame.sprite.Sprite):
    def __init__(self, pos, group, display_surface, name):
        super().__init__(group)

        self.display_surface = display_surface
        self.name = name
        self.image = pygame.Surface((10, 30), pygame.SRCALPHA)
        self.image.fill("black")

        self.start_x = pos[0]
        self.start_y = pos[1]
        # Draw a green circle on the image surface
        # pygame.draw.circle(self.image, (0, 255, 0), (32, 32), 32)

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)
        self.dragging = False  # Flag to track whether the slider is being dragged

        self.max = 2
        self.min = 0.25
        self.k = 1  # start value

        # Set range of slider
        self.a = (self.max - self.min) / (SLIDER_MAX - SLIDER_MIN)
        self.b = self.min - self.a * SLIDER_MIN

        self.rect.x = (self.k - self.b) / self.a

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
            if self.rect.collidepoint(mouse_pos):
                self.dragging = True
        elif mouse_click[0] == False:
            self.dragging = False

        if self.dragging:
            # Ensure the slider stays within its bounding box
            self.rect.centerx = max(self.rect.left, min(mouse_pos[0], self.rect.right))

        if self.rect.x < SLIDER_MIN:
            self.rect.x = SLIDER_MIN
        elif self.rect.x > SLIDER_MAX:
            self.rect.x = SLIDER_MAX

        self.k = self.a * self.rect.x + self.b

        # print(self.k)
        self.draw_value(self.display_surface)

    def draw_value(self, screen):
        # Draw the value of the slider (for demonstration purposes)
        font = pygame.font.Font(None, 24)
        value_text = font.render(f"{self.name}: {self.k:.2f}", True, (255, 255, 255))
        screen.blit(value_text, (1010, self.start_y - 35))
