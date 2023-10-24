import pygame 
from settings import *
from circle import Circle

class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		self.circle = Circle((300,300), self.all_sprites)

	def run(self,dt):
		self.display_surface.fill('white')
		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update(dt)