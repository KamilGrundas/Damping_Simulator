import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wyświetlanie Omegi")

# Wybór czcionki
font_size = 48
font = pygame.font.Font(None, font_size)

# Tworzenie tekstowej powierzchni
text = font.render("ω", True, (255, 255, 255))

# Główna pętla
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Czyszczenie ekranu i rysowanie tekstu
    screen.fill((0, 0, 0))
    screen.blit(text, (50, 50))
    pygame.display.flip()

# Zakończenie Pygame
pygame.quit()
sys.exit()
