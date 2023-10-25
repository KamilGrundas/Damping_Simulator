import pygame 
from settings import *
from circle import Circle
from spring import Spring

class Level:
	def __init__(self):

		self.pause = False

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		self.circle = Circle((SCREEN_WIDTH/2,300), self.all_sprites)
		self.spring = Spring((SCREEN_WIDTH/3,300), self.all_sprites)

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_p]:
			self.pause = True
		elif keys[pygame.K_c]:
			self.pause = False



	def run(self,dt):
		self.display_surface.fill('white')
		self.all_sprites.draw(self.display_surface)
		self.input()
		if self.pause == False:
			self.all_sprites.update(dt)