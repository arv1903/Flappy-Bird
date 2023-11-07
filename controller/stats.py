from json import load, dump

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

		with open(self.fileData) as f:
			data_load = load(f)

		return data_load

	def saveData(self):

		data = self.high_score
		data = round(data, -1)

		with open(self.fileData, "w") as f:
			dump(data,f)

		return data