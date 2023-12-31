import pygame
from random import randint

class Settings:

	def __init__(self):

		#game setting
		self.screen_width  = 400
		self.screen_height = 700
		self.title         = "FLAPPY BIRD"
		self.bg_color      = [230, 230, 230]
		self.bg_image      = pygame.image.load("img/bg.jpg")

		#bird setting
		self.bird_flying_speed = 3
		self.bird_drop_speed   = 1.5
		self.bird_life         = 1

		#floor setting
		self.floor_speed = 1

		#obstacle aetting
		
		self.obs_speed   = 1
		self.obs_gap     = 250

		#setting R pipe
		self.pipe_height = -1 * randint(10, 200) #-400

		#setting pipe
		self.pipe_depth  = self.pipe_height + 400 + self.obs_gap

		#point 
		self.point       = 0.05

	