import sys
import pygame as pyg
import gameobjects as go
from gameobjects import Bullet

def checkdown_events(event,ai_settings,screen,ship,bullets):
    if event.type == pyg.KEYDOWN:
        if event.key == pyg.K_RIGHT:
            ship.r_moving = True
        elif event.key == pyg.K_LEFT:
            ship.l_moving = True
        elif event.key == pyg.K_SPACE:
            fire_bullet(ai_settings,screen,ship,bullets)
    elif event.type == pyg.KEYUP:
        if event.key == pyg.K_RIGHT:
            ship.r_moving = False
        elif event.key == pyg.K_LEFT:
            ship.l_moving = False

def check_events(ai_settings,screen,ship,bullets):
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        checkdown_events(event,ai_settings,screen,ship,bullets)

def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pyg.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

