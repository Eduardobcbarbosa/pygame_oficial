import pygame
from config import screen, font_xl, font_medium, font_large, font_small, WHITE, RED, GREEN, BLACK, WIDTH
from assets import fundodetela_menu, fundodetela_game_over, fundodetela_phase1, fundodetela_phase2

def draw_menu():
    screen.blit(fundodetela_menu, (0, 0))  
    title = font_xl.render("Guerra contra a DP", True, WHITE)
    start = font_medium.render("Pressione 'ESPAÇO' para começar", True, RED)
    instructions = font_medium.render("Use as setinhas para mover e 'ESPAÇO' para atirar", True, WHITE)

    screen.blit(title, (400 - title.get_width() // 2, 150))
    screen.blit(start, (400 - start.get_width() // 2, 300))
    screen.blit(instructions, (400 - instructions.get_width() // 2, 350))

def draw_game_over(player):
    screen.blit(fundodetela_game_over, (0, 0))  
    text = font_large.render("GAME OVER", True, RED)
    score_text = font_medium.render(f"Pontuação: {player.score}", True, WHITE)
    restart = font_medium.render("Pressione ESPAÇO para recomeçar", True, GREEN)

    screen.blit(text, (400 - text.get_width() // 2, 200))
    screen.blit(score_text, (400 - score_text.get_width() // 2, 300))
    screen.blit(restart, (400 - restart.get_width() // 2, 350))

def draw_phase1(player, bullets, enemies, quizzes):
    screen.blit(fundodetela_phase1, (0, 0))  # Atualizado
    player.draw()
    
    for bullet in bullets:
        bullet.draw()
    
    for enemy in enemies:
        enemy.draw()
    
    for quiz in quizzes:
        quiz.draw()
    
    score_text = font_medium.render(f"Pontos: {player.score}", True, BLACK)
    lives_text = font_medium.render(f"Vidas: {player.lives}", True, BLACK)
    phase_text = font_small.render("Fase 1", True, BLACK)

    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 50))
    screen.blit(phase_text, (WIDTH - 100, 20))

def draw_phase2(player, bullets, enemies, quizzes):
    screen.blit(fundodetela_phase2, (0, 0))  # Atualizado
    player.draw()
    
    for bullet in bullets:
        bullet.draw()
    
    for enemy in enemies:
        enemy.draw()
    
    for quiz in quizzes:
        quiz.draw()
    
    score_text = font_medium.render(f"Pontos: {player.score}", True, BLACK)
    lives_text = font_medium.render(f"Vidas: {player.lives}", True, BLACK)
    phase_text = font_small.render("Fase 2", True, BLACK)

    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 50))
    screen.blit(phase_text, (WIDTH - 100, 20))