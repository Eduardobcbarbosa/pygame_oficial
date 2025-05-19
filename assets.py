import pygame

# Inicializa o pygame (importante para carregar imagens)
pygame.init()

# Carrega as imagens
fundodetela_menu = pygame.image.load('assets/tela_inicial.png').convert()
fundodetela_menu = pygame.transform.scale(fundodetela_menu, (800, 600))
fundodetela_phase1 = pygame.image.load('assets/tela_phase1.png').convert()
fundodetela_phase1 = pygame.transform.scale(fundodetela_phase1, (800, 600))
fundodetela_phase2 = pygame.image.load('assets/tela_phase2.png').convert()
fundodetela_phase2 = pygame.transform.scale(fundodetela_phase2, (800, 600))
fundodetela_game_over = pygame.image.load('assets/tela_game_over.png').convert()
fundodetela_game_over = pygame.transform.scale(fundodetela_game_over, (800, 600))
fundodetela_victory = pygame.image.load('assets/tela_victory.png').convert()
fundodetela_victory = pygame.transform.scale(fundodetela_victory, (800, 600))
jogador = pygame.image.load('assets/player.png').convert()