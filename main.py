import pygame
import random
import sys
from config import *
from assets import *
from sprites import Player, Bullet, Enemy, QuizWord, Heart
from game_screen import draw_menu, draw_game_over, draw_phase1, draw_phase2

player = Player()
bullets = []
enemies = []
quizzes = []
heart = Heart()
game_state = MENU
enemy_spawn_timer = 0
quiz_spawn_timer = 0
heart_spawn_timer = 0
enemies_killed_in_phase2 = 0

running = True
clock = pygame.time.Clock()
FPS = 60

def reset_game():
    global player, bullets, enemies, quizzes, heart, game_state, enemy_spawn_timer, quiz_spawn_timer, heart_spawn_timer, enemies_killed_in_phase2
    player = Player()
    bullets = []
    enemies = []
    quizzes = []
    heart = Heart()
    game_state = MENU
    enemy_spawn_timer = 0
    quiz_spawn_timer = 0
    heart_spawn_timer = 0
    enemies_killed_in_phase2 = 0

def start_phase1():
    global game_state
    game_state = PHASE1
    player.score = 0
    player.lives = 3

def start_phase2():
    global game_state
    game_state = PHASE2

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
                    start_phase1()
                elif game_state in (GAME_OVER, VICTORY):
                    reset_game()
                elif game_state in (PHASE1, PHASE2):
                    player.shoot()
    
    if game_state == MENU:
        draw_menu()
    elif game_state == PHASE1:
        draw_phase1(player, bullets, enemies, quizzes)
    elif game_state == PHASE2:
        draw_phase2(player, bullets, enemies, quizzes)
    elif game_state == GAME_OVER:
        draw_game_over(player)
    
    pygame.display.flip()

pygame.quit()
sys.exit()

