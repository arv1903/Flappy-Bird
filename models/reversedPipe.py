import pygame
from random import randint

class ReversedPipe:

	def __init__(self, info_game):

		self.screen      = info_game.screen
		self.setting     = info_game.game_setting

		self.screen_rect = info_game.screen.get_rect()

		self.image       = pygame.image.load("img/reversedPipe.PNG")

		self.rect        = self.image.get_rect()

		self.rect.y      = self.setting.pipe_height
		self.rect.x      = self.setting.screen_width

	def update(self):
		self.rect.x    -= self.setting.obs_speed
		self.blitme()
		if self.rect.x <= -70:
			self.rect.y = -1 * randint(10, 350)
			self.rect.x = 500

	def blitme(self):
		self.screen.blit(self.image, self.rect)