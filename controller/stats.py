import sqlite3

class GameStatistics:

	def __init__(self, info_game):

		self.fileData   = 'highscore.json'
		self.setting    = info_game.game_setting

		self.reset_statistics()

		self.game_active = False
		self.high_score  = self.loadData()


	def reset_statistics(self):

		self.current_level_score = 0
		self.score               = 0
		self.level               = 1

	####################
	#LOAD AND SAVE DATA#
	####################

	def loadData(self):
		conn = sqlite3.connect('highscore.db')
		c    = conn.cursor()
		with conn:
			c.execute("""
				CREATE TABLE IF NOT EXISTS highscore (
					highscore INTEGER NOT NULL
				);
			""")
		conn.commit()		
		c.execute("SELECT * FROM highscore")
		highscore = max(c.fetchone()[0], round(self.score,-1))
		with conn:
			c.execute(f"UPDATE highscore SET highscore = {highscore}")

		return highscore