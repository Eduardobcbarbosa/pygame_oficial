import pygame
import sys
from config import WIDTH, HEIGHT, MENU, PHASE1, PHASE2, GAME_OVER, VICTORY
from assets import fundodetela_menu, fundodetela_game_over
from game_screen import draw_menu, draw_game_over
#from sprites import Player, Bullet, Enemy, QuizWord, Heart


pygame.init()
pygame.mixer.init()


game_state = MENU
running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            if event.key == pygame.K_SPACE:
                if game_state == MENU:
                    game_state = PHASE1
                elif game_state == GAME_OVER:
                    game_state = MENU
    
    if game_state == MENU:
        draw_menu()
    elif game_state == GAME_OVER:
        draw_game_over(None) 
    
    pygame.display.flip()
pygame.quit()
sys.exit()

