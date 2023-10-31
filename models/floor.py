import pygame

class Floor:

	def __init__(self, info_game):

		self.screen      = info_game.screen
		self.setting     = info_game.game_setting

		self.screen_rect = info_game.screen.get_rect()

		self.image       = pygame.image.load("img/floor.PNG")

		self.rect        = self.image.get_rect()

		self.rect.right  = self.screen_rect.right
		self.rect.bottom = self.screen_rect.bottom

	def update(self):
		self.rect.x    -= self.setting.floor_speed
		self.blitme()
		if self.rect.x <= -400:
			self.rect.x = -10

	def blitme(self):
		self.screen.blit(self.image, self.rect)