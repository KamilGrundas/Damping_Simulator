import pygame
from settings import *

class Slider(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((10, 30), pygame.SRCALPHA)
        self.image.fill("black")
        
        # Draw a green circle on the image surface
        #pygame.draw.circle(self.image, (0, 255, 0), (32, 32), 32)

        # Set the position of the sprite
        self.rect = self.image.get_rect(center=pos)
        self.dragging = False  # Flag to track whether the slider is being dragged
        self.value = 0.5  # Initial value (between 0 and 1)

        self.k = 1


    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.rect.x < SCREEN_WIDTH-SIDE_MENU_WIDTH + 30:
            self.rect.x = SCREEN_WIDTH-SIDE_MENU_WIDTH + 30
        elif self.rect.x > SCREEN_WIDTH - 30:
            self.rect.x = SCREEN_WIDTH - 30

        if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
            if self.rect.collidepoint(mouse_pos):
                self.dragging = True
        elif mouse_click[0] == False:
            self.dragging = False

        if self.dragging:
            
            # Ensure the slider stays within its bounding box
            self.rect.centerx = max(self.rect.left, min(mouse_pos[0], self.rect.right))
        
        self.k = self.rect.x/1000

    def draw_value(self, screen):
        # Draw the value of the slider (for demonstration purposes)
        font = pygame.font.Font(None, 36)
        value_text = font.render(f"{self.value:.2f}", True, (255, 255, 255))
        screen.blit(value_text, (self.rect.right + 10, self.rect.centery - value_text.get_height() // 2))
