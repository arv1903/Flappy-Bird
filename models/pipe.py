import pygame
from random import randint

class Pipe:

	def __init__(self, info_game):

		self.screen        = info_game.screen
		self.setting       = info_game.game_setting
 
		self.screen_rect   = info_game.screen.get_rect()

		self.image         = pygame.image.load("img/pipe.PNG")

		self.rect          = self.image.get_rect()

		self.rect.y        = self.setting.pipe_depth
		self.rect.x        = self.setting.screen_width

		self.reversed_pipe = info_game.rPipe

	def update(self):
		self.rect.x    -= self.setting.obs_speed
		self.blitme()
		if self.rect.x <= -70:
			#self.rect.y = self.reversed_pipe.rect.y + self.setting.obs_gap + 430 + 100
			self.rect.y = self.reversed_pipe.rect.y + 400 + self.setting.obs_gap
			self.rect.x = 500

	def blitme(self):
		self.screen.blit(self.image, self.rect)