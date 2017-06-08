import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """init of the ship and its starting position"""
        self.screen = screen
        # Load the ship and gets its rect.
        self.image = pygame.image.load_extended('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        super(Ship, self).__init__()

        # start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal for the Ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's movement based on the movement flag"""
        # update the ships value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
