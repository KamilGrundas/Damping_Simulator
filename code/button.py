import pygame
from settings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.play_image = pygame.image.load(PLAY_BUTTON).convert_alpha()
        self.replay_image = pygame.image.load(REPLAY_BUTTON).convert_alpha()
        self.play_image_resized = pygame.transform.scale(self.play_image, (100, 100))
        self.replay_image_resized = pygame.transform.scale(
            self.replay_image, (100, 100)
        )
        self.image = self.play_image_resized
        self.rect = self.image.get_rect(center=pos)
        self.is_playing = True  # Track whether the button is in play state
        self.last_state_change_time = pygame.time.get_ticks()
        self.cooldown_duration = 250  # Cooldown duration in milliseconds (0.5 seconds)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_state_change_time >= self.cooldown_duration:
                self.toggle_state()
                self.last_state_change_time = current_time

    def toggle_state(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.image = self.play_image_resized
            # Add code here to handle play state
        else:
            self.image = self.replay_image_resized
            # Add code here to handle pause state
