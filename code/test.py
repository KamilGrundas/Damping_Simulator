import pygame
from settings import *

class Slider(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.slider_image = pygame.image.load(PLAY_BUTTON).convert_alpha()
        self.image = self.slider_image  # Added this line to fix the AttributeError
        self.rect = self.slider_image.get_rect(center=pos)
        self.dragging = False  # Flag to track whether the slider is being dragged
        self.value = 0.5  # Initial value (between 0 and 1)


    def update(self):
        if self.dragging:
            mouse_x, _ = pygame.mouse.get_pos()
            # Ensure the slider stays within its bounding box
            self.rect.centerx = max(self.rect.left, min(mouse_x, self.rect.right))

    def draw_value(self, screen):
        # Draw the value of the slider (for demonstration purposes)
        font = pygame.font.Font(None, 36)
        value_text = font.render(f"{self.value:.2f}", True, (255, 255, 255))
        screen.blit(value_text, (self.rect.right + 10, self.rect.centery - value_text.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.update()


# class Button(pygame.sprite.Sprite):
#     def __init__(self, pos, group, slider):
#         super().__init__(group)

#         self.play_image = pygame.image.load(PLAY_BUTTON).convert_alpha()
#         self.pause_image = pygame.image.load(PAUSE_BUTTON).convert_alpha()
#         self.image = self.play_image
#         self.rect = self.image.get_rect(center=pos)
#         self.is_playing = True  # Track whether the button is in play state
#         self.last_state_change_time = pygame.time.get_ticks()
#         self.cooldown_duration = 250  # Cooldown duration in milliseconds (0.5 seconds)
#         self.slider = slider

#     def update(self):
#         mouse_pos = pygame.mouse.get_pos()
#         mouse_click = pygame.mouse.get_pressed()

#         if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
#             current_time = pygame.time.get_ticks()
#             if current_time - self.last_state_change_time >= self.cooldown_duration:
#                 self.toggle_state()
#                 self.last_state_change_time = current_time

#     def toggle_state(self):
#         self.is_playing = not self.is_playing
#         if self.is_playing:
#             self.image = self.play_image
#             # Add code here to handle play state
#         else:
#             self.image = self.pause_image
#             # Add code here to handle pause state


# Example usage:

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slider Demo")

all_sprites = pygame.sprite.Group()

slider = Slider((400, 300), all_sprites)
# button = Button((400, 400), all_sprites, slider)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        slider.handle_event(event)

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    slider.draw_value(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()