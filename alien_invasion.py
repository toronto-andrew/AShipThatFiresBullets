import sys
import pygame
from settings import Settings   # 导入Settings类
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()    # 创建Settings实例
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()       # 更新飞船位置      
        gf.update_screen(ai_settings, screen, ship) 

run_game()
