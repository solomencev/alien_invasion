class GameStats():
	"""Отслеживание статистики для игры"""
	def __init__(self, ai_settings):
		"""Инициализирует статистику"""
		self.ai_settings = ai_settings
		self.reset_stats()
		#Игра запускается в активном состоянии
		self.game_active = True
		
		#Игра запускается в неактивном состоянии
		self.game_active= False
		#Рекорд не должен сбрасываться
		self.high_score = 0
		
	def reset_stats(self):
		"""инициализирует статистику, изменяющуюся в ходе игры"""
		self. ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
