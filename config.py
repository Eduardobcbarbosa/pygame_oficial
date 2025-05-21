import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guerra contra a DP")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

font_xl = pygame.font.SysFont('Arial', 75)
font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 20)

MENU = 0
PHASE1 = 1
PHASE2 = 2
GAME_OVER = 3
VICTORY = 4

MENU_MUSIC = "assets/sounds/menu_music.mp3"
PHASE1_MUSIC = "assets/sounds/phase1_music.mp3"
PHASE2_MUSIC = "assets/sounds/phase2_music.mp3"
VICTORY_MUSIC = "assets/sounds/victory_music.mp3"
GAME_OVER_MUSIC = "assets/sounds/game_over_music.mp3"
SHOT_SOUND = "assets/sounds/shot_sound.wav"


 