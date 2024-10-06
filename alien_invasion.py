import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Alien Invasion")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()        
    #print("game run")

run_game()
