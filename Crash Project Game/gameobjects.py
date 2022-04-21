import pygame as pyg

from pygame.sprite import Sprite

class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.caption = "Alien Invasion"
        self.ship_speed_factor = 0.1
        self.bullet_speed_factor = 1
        self.bullet_width = 50
        self.bullet_height = 50
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

class Ship():

    def __init__(self,screen,ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pyg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.center = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.r_moving = False
        self.l_moving = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.r_moving and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.l_moving and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

class Bullet():
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen

        self.rect = pyg.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        pyg.draw.rect(self.screen,self.color,self.rect)
