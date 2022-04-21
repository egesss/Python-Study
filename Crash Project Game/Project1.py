# C:\Users\egese\AppData\Roaming\Python\Python37\site-packages\pygame\examples

import gamefunctions as gf
import gameobjects as go
import pygame as pyg
from pygame.sprite import Group

def run_game():

    ai_settings = go.Settings()
    screen = pyg.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pyg.display.set_caption(ai_settings.caption)
    ship = go.Ship(screen,ai_settings)

    bullets = Group()

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()