import pygame
from settings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, group, active, deactive):
        super().__init__(group)

        self.deactive_image = pygame.image.load(deactive).convert_alpha()
        self.active_image = pygame.image.load(active).convert_alpha()

        self.image = self.deactive_image
        self.rect = self.image.get_rect(center=pos)
        self.is_playing = True  # Track whether the button is in play state
        self.last_state_change_time = pygame.time.get_ticks()
        self.cooldown_duration = 250  # Cooldown duration in milliseconds (0.5 seconds)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        self.toggle_state()

        if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_state_change_time >= self.cooldown_duration:
                self.is_playing = not self.is_playing
                self.last_state_change_time = current_time

    def toggle_state(self):
        if self.is_playing:
            self.image = self.deactive_image
            # Add code here to handle play state
        else:
            self.image = self.active_image
            # Add code here to handle pause state
