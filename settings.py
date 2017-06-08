class Settings():
	'''A class to store all settings for the game'''
	def __init__(self):
		''' init of game settings'''
		#screen settings
		self.screen_width = 1200
		self.screen_height =800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed_factor = 1.5

		#bullet Settings 
		self.bullet_speed_factor = 3
		self.bullet_width  = 100
		self.bullet_height = 15
		self.bullet_color = 60,60, 60
		self.bullets_allowed = 5

		self.alien_speed_factor = 1

		self.fleet_drop_speed=30
		self.fleet_direction = 1
		self.ship_limit = 3

		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self. initalize_dynamic_settings()
	def initalize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.alien_points = 50
		#Directions 1 represents right and -1 represents left.
		self.fleet_direction = 1
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor*= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points* self.score_scale)
		print(self.alien_points)










