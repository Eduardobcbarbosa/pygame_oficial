import pygame
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guerra contra a DP")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MENU = 0
PHASE1 = 1
GAME_OVER = 2
game_state = MENU

assets = {
    "FASE1_IMG": pygame.image.load('assets/tela_phase1.png'),
    "MENU_IMG": pygame.image.load('assets/tela_inicial.png'),
    "GAME_OVER_IMG": pygame.image.load('assets/tela_game_over.png')
}

def draw_menu():
    screen.blit(assets["MENU_IMG"], (0, 0))

def draw_game_over():
    screen.blit(assets["GAME_OVER_IMG"], (0, 0))

def draw_phase1():
    screen.blit(assets["FASE1_IMG"], (0, 0))

running = True
while running:
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
        draw_game_over()
    elif game_state == PHASE1:
        draw_phase1()

    pygame.display.flip()

pygame.quit()
sys.exit()
