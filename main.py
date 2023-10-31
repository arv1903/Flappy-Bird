import pygame
import sys
from   random    import randint
from   json      import load,dump
import time

from controller import settings
from models     import bird, floor


class Game:

	def __init__(self):

		pygame.init()

		self.finish       = False

		self.game_setting = settings.Settings()
		self.screen       = pygame.display.set_mode([self.game_setting.screen_width, self.game_setting.screen_height])
		self.title        = pygame.display.set_caption(self.game_setting.title)
		self.bg_color     = self.game_setting.bg_color
		self.bg_image     = self.game_setting.bg_image

		self.game_setting.screen_width  = self.screen.get_rect().width
		self.game_setting.screen_height = self.screen.get_rect().height
		
		self.bird     = bird.Bird(self)
		self.floor    = floor.Floor(self)

	
	def run_game(self):

		while not self.finish:
			self.events()
			self.update()
			
			self.bird.update()
			self.floor.update()

			self.bird.update()
			self.floor.update()
			self.check_floor()		

	def check_floor(self):
		if self.bird.rect.bottom < (self.game_setting.screen_height - 100):
			self.bird.bird_drop()

	def events(self):

		for event in pygame.event.get():
			if event.type   == pygame.QUIT:
				sys.exit()
				
			elif event.type == pygame.KEYDOWN:
				self.check_keydown(event)

			elif event.type == pygame.KEYUP:
				self.check_keyup(event)

	def check_keydown(self, event):

		if event.key == pygame.K_q:
			sys.exit()

		if event.key == pygame.K_SPACE:
			self.bird.moving_up = True

	def check_keyup(self, event):

		if event.key == pygame.K_SPACE:
			self.bird.moving_up = False
			
	def update(self):
		self.screen.blit(self.bg_image, (0,0))
		self.bird.blitme()
		self.floor.blitme()
		pygame.display.flip()


if __name__ == "__main__":
	game = Game()
	game.run_game()