import pygame 
from settings import *
from circle import Circle
from spring import Spring
from silencer import Silencer
from connector import Connector
from side_menu import SideMenu

class Level:
	def __init__(self):

		self.pause = False


		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		self.side_menu = SideMenu((SCREEN_WIDTH-SIDE_MENU_WIDTH/2,SCREEN_HEIGHT/2), self.all_sprites)
		self.circle = Circle((SCREEN_WIDTH/2 -32,300), self.all_sprites)
		self.spring = Spring((SCREEN_WIDTH/2,10),self.circle, self.all_sprites)
		self.silencer = Silencer((SCREEN_WIDTH/2 - 64,100),self.circle, self.all_sprites)
		self.connector = Connector((SCREEN_WIDTH/2 - 63,100),self.circle, self.all_sprites)

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_p]:
			self.pause = True
		elif keys[pygame.K_c]:
			self.pause = False
			self.spring.show_graph = False
		elif keys[pygame.K_w]:

			self.spring.show_graph = True



	def run(self,dt):
		self.display_surface.fill('white')
		self.all_sprites.draw(self.display_surface)
		self.input()
		if self.pause == False:
			self.all_sprites.update(dt)

