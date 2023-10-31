import pygame

class Bird:

	def __init__(self, info_game):

		self.screen       = info_game.screen
		self.setting      = info_game.game_setting

		self.screen_rect  = info_game.screen.get_rect()

		self.image        = pygame.image.load("img/bird.PNG")

		self.rect         = self.image.get_rect() 
		self.rect.midleft = self.screen_rect.midleft
		self.rect.x       = 10

		self.x            = float(self.rect.x)
		self.y            = float(self.rect.y)

		self.moving_up    = False

	def update(self):		
		if self.moving_up and (self.rect.top > 0):
			self.y -= self.setting.bird_flying_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def bird_drop(self):
		self.y     += self.setting.bird_drop_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)