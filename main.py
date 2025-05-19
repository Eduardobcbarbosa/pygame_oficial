import pygame
import random
import sys
from config import *
from assets import *
from sprites import Player, Bullet, Enemy, QuizWord, Heart
from game_screen import draw_menu, draw_game_over, draw_phase1, draw_phase2, draw_victory

# Inicialização do jogo
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

# Funções de controle
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

# Loop principal
running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    clock.tick(FPS)

    # Eventos
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
    
    # Lógica do jogo
    if game_state == PHASE1:
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        # Controle de tiros
        if keys[pygame.K_SPACE]:
            player.shoot(bullets)

        # Spawn de inimigos
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= 60:
            enemies.append(Enemy(1.3))
            enemy_spawn_timer = 0

        # Spawn de palavras QUIZ
        quiz_spawn_timer += 1
        if quiz_spawn_timer >= 180:
            quizzes.append(QuizWord(1.5))
            quiz_spawn_timer = 0

        # Atualização de balas
        for bullet in bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                bullets.remove(bullet)

        # Atualização de inimigos
        for enemy in enemies[:]:
            enemy.update()
            colidiu_com_bala_inimigo = False
            if enemy.is_past_line():
                enemies.remove(enemy)
                player.lives -= 1
                if player.lives <= 0:
                    game_state = GAME_OVER
            else:
                for bullet in bullets[:]:
                    if not colidiu_com_bala_inimigo and (
                        bullet.x < enemy.x + enemy.width and
                        bullet.x + bullet.width > enemy.x and
                        bullet.y < enemy.y + enemy.height and
                        bullet.y + bullet.height > enemy.y
                    ):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        player.score += 1
                        colidiu_com_bala_inimigo = True
                        if player.score >= 20:
                            start_phase2()

        # Atualização de palavras QUIZ
        for quiz in quizzes[:]:
            quiz.update()
            colidiu_com_bala_quiz = False
            if quiz.is_past_line():
                quizzes.remove(quiz)
            else:
                for bullet in bullets[:]:
                    if not colidiu_com_bala_quiz and (
                        bullet.x < quiz.x + quiz.width and
                        bullet.x + bullet.width > quiz.x and
                        bullet.y < quiz.y + quiz.height and
                        bullet.y + bullet.height > quiz.y
                    ):
                        bullets.remove(bullet)
                        quizzes.remove(quiz)
                        player.lives -= 1
                        colidiu_com_bala_quiz = True
                        if player.lives <= 0:
                            game_state = GAME_OVER
    
    elif game_state == PHASE2:
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        # Controle de tiros
        if keys[pygame.K_SPACE]:
            player.shoot(bullets)

        # Spawn de inimigos
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= 40:
            enemies.append(Enemy(2.3))
            enemy_spawn_timer = 0

        # Spawn de palavras QUIZ
        quiz_spawn_timer += 1
        if quiz_spawn_timer >= 120:
            quizzes.append(QuizWord(2))
            quiz_spawn_timer = 0

        # Spawn de corações
        if not heart.active:
            heart_spawn_timer += 1
            if heart_spawn_timer >= 900:
                heart.active = True
                heart_spawn_timer = 0
                heart.x = random.randint(50, WIDTH - 200)
                heart.y = random.randint(50, HEIGHT - 50)

        # Atualização de balas
        for bullet in bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                bullets.remove(bullet)

        # Atualização de inimigos
        for enemy in enemies[:]:
            enemy.update()
            colidiu_com_bala_inimigo_fase2 = False
            if enemy.is_past_line():
                enemies.remove(enemy)
                player.lives -= 1
                if player.lives <= 0:
                    game_state = GAME_OVER
            else:
                for bullet in bullets[:]:
                    if not colidiu_com_bala_inimigo_fase2 and (
                        bullet.x < enemy.x + enemy.width and
                        bullet.x + bullet.width > enemy.x and
                        bullet.y < enemy.y + enemy.height and
                        bullet.y + bullet.height > enemy.y
                    ):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        player.score += 1
                        enemies_killed_in_phase2 += 1
                        colidiu_com_bala_inimigo_fase2 = True

                        if enemies_killed_in_phase2 >= 15:
                            heart.active = True
                            enemies_killed_in_phase2 = 0
                            heart.x = random.randint(50, WIDTH - 200)
                            heart.y = random.randint(50, HEIGHT - 50)

                        if player.score >= 50:
                            game_state = VICTORY

        # Atualização de palavras QUIZ
        for quiz in quizzes[:]:
            quiz.update()
            colidiu_com_bala_quiz_fase2 = False
            if quiz.is_past_line():
                quizzes.remove(quiz)
            else:
                for bullet in bullets[:]:
                    if not colidiu_com_bala_quiz_fase2 and (
                        bullet.x < quiz.x + quiz.width and
                        bullet.x + bullet.width > quiz.x and
                        bullet.y < quiz.y + quiz.height and
                        bullet.y + bullet.height > quiz.y
                    ):
                        bullets.remove(bullet)
                        quizzes.remove(quiz)
                        player.lives -= 1
                        colidiu_com_bala_quiz_fase2 = True
                        if player.lives <= 0:
                            game_state = GAME_OVER

        # Atualização do coração
        if heart.active:
            heart.update()
            colidiu_com_bala_coracao = False
            if heart.is_past_line():
                heart.active = False
            else:
                for bullet in bullets[:]:
                    if not colidiu_com_bala_coracao and (
                        bullet.x < heart.x + heart.width and
                        bullet.x + bullet.width > heart.x and
                        bullet.y < heart.y + heart.height and
                        bullet.y + bullet.height > heart.y
                    ):
                        bullets.remove(bullet)
                        heart.active = False
                        player.lives += 1
                        colidiu_com_bala_coracao = True

    # Renderização
    if game_state == MENU:
        draw_menu()
    elif game_state == PHASE1:
        draw_phase1(player, bullets, enemies, quizzes)
    elif game_state == PHASE2:
        draw_phase2(player, bullets, enemies, quizzes)
    elif game_state == GAME_OVER:
        draw_game_over(player)
    elif game_state == VICTORY:
        draw_victory(player)

    pygame.display.flip()

pygame.quit()
sys.exit()