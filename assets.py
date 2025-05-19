import pygame

pygame.init()

#fundodetela_menu = pygame.image.load('assets/tela_incial.png')
#fundodetela_phase1 = pygame.image.load('assets/tela_phase1.png')
#fundodetela_phase2 = pygame.image.load('assets/tela_phase2.png')
#fundodetela_game_over = pygame.image.load('assets/tela_game_over.png')

fundodetela_menu = 'tela_inicial'
fundodetela_phase1 = 'tela_phase1'
fundodetela_phase2 = 'tela_phase2'
fundodetela_game_over = 'tela_game_over'
fundodetela_victory = 'tela_victory'

def load_assets():
    assets = {}
    assets[fundodetela_menu] = pygame.image.load('assets/tela_incial.png').convert()
    assets[fundodetela_phase1] = pygame.image.load('assets/tela_phase1.png').convert()
    assets[fundodetela_phase2] = pygame.image.load('assets/tela_phase2.png').convert()
    assets[fundodetela_game_over] = pygame.image.load('assets/tela_game_over.png').convert()
    assets[fundodetela_victory] = pygame.image.load('assets/tela_victory.png').convert()