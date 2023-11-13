import pygame, sys
from settings import *
from level import Level

class Simulator:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('SZPN')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick(60) / 1000
			#print(self.clock.get_fps())
			self.level.run(dt)
			pygame.display.update()

if __name__ == '__main__':
	simulator = Simulator()
	simulator.run()
