import pygame, sys
from settings import *
from menu import Menu


class Simulator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("SZPN")
        self.clock = pygame.time.Clock()
        self.menu = Menu()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(100)
            self.menu.run(int(self.clock.get_fps()))
            # print(self.clock.get_fps())
            # self.level.run(int(self.clock.get_fps()))
            pygame.display.update()


if __name__ == "__main__":
    simulator = Simulator()
    simulator.run()
