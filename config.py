import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # tamanho da tela
pygame.display.set_caption("Guerra contra a DP") #titulo do jogo
# define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
# tamanho e fonte letra
font_xl = pygame.font.SysFont('Arial', 75)
font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 20)
#ordem das telas 
MENU = 0
PHASE1 = 1
PHASE2 = 2
GAME_OVER = 3
VICTORY = 4
#musicas
MENU_MUSIC = "assets/sounds/menu_music.wav"
PHASE1_MUSIC = "assets/sounds/phase1_music.wav"
PHASE2_MUSIC = "assets/sounds/phase2_music.wav"
VICTORY_MUSIC = "assets/sounds/victory_music.wav"
GAME_OVER_MUSIC = "assets/sounds/game_over_music.wav"
SHOT_SOUND = "assets/sounds/shot_sound.wav"


 