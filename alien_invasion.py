import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from game_stats import GameStats
import game_functions as gf
from scoreboard import Scoreboard



def run_game():
	#init of the game, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_settings, screen, "play")
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	# Make a ship
	ship = Ship(ai_settings,screen)
	#Make an Alien
	aliens = Alien(ai_settings,screen)

	#Make bullets into a group
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Start the main loop for the game
	while True:
		gf.check_events(ai_settings, screen,stats,sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings,screen,stats, sb,ship, aliens, bullets)
		gf.update_screen(ai_settings,screen,stats, sb , ship, aliens, bullets,play_button)


run_game()



