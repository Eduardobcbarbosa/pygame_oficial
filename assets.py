import pygame

pygame.init()

#fundodetela_menu = pygame.image.load('assets/tela_incial.png')
#fundodetela_phase1 = pygame.image.load('assets/tela_phase1.png')
#fundodetela_phase2 = pygame.image.load('assets/tela_phase2.png')
#fundodetela_game_over = pygame.image.load('assets/tela_game_over.png')

BACKGROUND = 'tela_inicial'
FASE1_IMG = 'tela_phase1'
FASE2_IMG = 'tela_phase2'
GAME_OVER = 'tela_game_over'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load('assets/tela_incial.png').convert()
    assets[FASE1_IMG] = pygame.image.load('assets/tela_phase1.png').convert()
    assets[FASE2_IMG] = pygame.image.load('assets/tela_phase2.png').convert()
    assets[GAME_OVER] = pygame.image.load('assets/tela_game_over.png').convert()