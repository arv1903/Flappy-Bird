import pygame
import sys

from models     import bird, floor, pipe, reversedPipe
from controller import settings, button, stats, score

class Game:

	def __init__(self):

		pygame.init()

		self.error         = False
		self.game_setting  = settings.Settings()
		self.stats         = stats.GameStatistics(self)
		self.screen        = pygame.display.set_mode([self.game_setting.screen_width, self.game_setting.screen_height])
		self.screen_rect   = self.screen.get_rect()
		self.title         = pygame.display.set_caption(self.game_setting.title)
		self.bg_image      = self.game_setting.bg_image
		self.bird          = bird.Bird(self)
		self.floor         = floor.Floor(self)
		self.rPipe         = reversedPipe.ReversedPipe(self)
		self.nPipe         = pipe.Pipe(self)
		self.play_button   = button.Button(self, "PLAY")
		self.score_board   = score.Scoreboard(self)

		self.game_setting.screen_width  = self.screen.get_rect().width
		self.game_setting.screen_height = self.screen.get_rect().height

	def run(self):

		while not self.error:
			self.events()

			if self.stats.game_active:
				
				self.bird.update()

				self.check_floor()
				self.floor.update()

				self.rPipe.update()
				self.nPipe.update()

				self.bird_fall()
				self.check_score()

				self.stats.level += 0.001 
				self.score_board.show_level()

				self.level()
				self.stats.loadData()

			self.update()

	def events(self):

		for event in pygame.event.get():
			if event.type   == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self.keyDown(event)

			elif event.type == pygame.KEYUP:
				self.keyUp(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.buttonPressed(pygame.mouse.get_pos())

	def keyDown(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		if event.key == pygame.K_SPACE:
			if not self.stats.game_active:
				self.stats.game_active = True
			self.bird.moving_up = True

	def keyUp(self, event):
		if event.key == pygame.K_SPACE:
			self.bird.moving_up = False

	def game_over(self):
		self.stats.game_active = False
		pygame.mouse.set_visible(True)

	def update(self):

		pygame.time.Clock().tick(1500)
		
		self.screen.blit(self.bg_image, (0,0))

		self.bird.blitme()

		self.rPipe.blitme()
		self.nPipe.blitme()

		self.floor.blitme()
		self.score_board.draw_score()

		if not self.stats.game_active:
			self.play_button._draw_button()

		pygame.display.flip()

	def buttonPressed(self, mouse_pos):

		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		status         = self.stats.game_active

		self.game_setting.bird_life = 1

		if button_clicked and not status:

			self.bird = bird.Bird(self)
			self.bird.reset_pos()

			self.stats.reset_statistics()
			self.stats.game_active        = True

			self.game_setting.obs_speed   = 1
			self.game_setting.floor_speed = 1

			self.score_board.show_score()

			self.nPipe.rect.x     = 500
			self.rPipe.rect.x     = 500

			pygame.mouse.set_visible(False)

	def check_floor(self):

		if self.bird.rect.bottom < (self.game_setting.screen_height - 100):
			self.bird.bird_drop()

	def level(self):

		self.game_setting.obs_speed   += (self.stats.level / 100000)
		self.game_setting.floor_speed += (self.stats.level / 100000)

	def check_score(self):

		self.stats.score += self.game_setting.point

		self.score_board.show_score()
		self.score_board.check_high_score()

	def bird_fall(self):

		collision1 = self.bird.rect.colliderect(self.nPipe)
		collision2 = self.bird.rect.colliderect(self.rPipe)

		if collision1 or collision2:
			self.game_setting.bird_life    -= 1

			if self.game_setting.bird_life == 0:
				self.check_score()
				self.game_over()

if __name__ == "__main__":
	Game().run()