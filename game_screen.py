import pygame
from config import screen, font_xl, font_medium, font_large, font_small, WHITE, RED, GREEN, BLACK, WIDTH, HEIGHT
from assets import fundodetela_menu, fundodetela_game_over, fundodetela_phase1, fundodetela_phase2, fundodetela_victory

def draw_menu():
    screen.blit(fundodetela_menu, (0, 0))  
    title = font_xl.render("Guerra contra a DP", True, WHITE)
    start = font_medium.render("Pressione 'ESPAÇO' para começar", True, RED)
    instructions = font_medium.render("Use as setinhas para mover e 'ESPAÇO' para atirar", True, WHITE)

    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//3))
    screen.blit(start, (WIDTH//2 - start.get_width()//2, HEIGHT//2))
    screen.blit(instructions, (WIDTH//2 - instructions.get_width()//2, HEIGHT//2 + 50))

def draw_game_over(player):
    screen.blit(fundodetela_game_over, (0, 0))  
    text = font_large.render("GAME OVER", True, RED)
    score_text = font_medium.render(f"Pontuação: {player.score}", True, WHITE)
    restart = font_medium.render("Pressione ESPAÇO para recomeçar", True, GREEN)

    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//3))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 50))

def draw_phase1(player, bullets, enemies, quizzes):
    screen.blit(fundodetela_phase1, (0, 0))

    player.draw(screen)
    
    for bullet in bullets:
        bullet.draw(screen)
    
    for enemy in enemies:
        enemy.draw(screen)
    
    for quiz in quizzes:
        quiz.draw(screen)

    
    score_text = font_medium.render(f"Pontos: {player.score}", True, BLACK)
    lives_text = font_medium.render(f"Vidas: {player.lives}", True, BLACK)
    phase_text = font_small.render("Fase 1", True, BLACK)

    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 50))
    screen.blit(phase_text, (WIDTH - 100, 20))

def draw_phase2(player, bullets, enemies, quizzes):
    screen.blit(fundodetela_phase2, (0, 0))  
    player.draw(screen)
    
    for bullet in bullets:
        bullet.draw(screen)
    
    for enemy in enemies:
        enemy.draw(screen)
    
    for quiz in quizzes:
        quiz.draw(screen)
    
    score_text = font_medium.render(f"Pontos: {player.score}", True, BLACK)
    lives_text = font_medium.render(f"Vidas: {player.lives}", True, BLACK)
    phase_text = font_small.render("Fase 2", True, BLACK)

    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 50))
    screen.blit(phase_text, (WIDTH - 100, 20))

def draw_victory(player):
    screen.blit(fundodetela_victory, (0, 0))  
    text = font_large.render("VITÓRIA!", True, GREEN)
    score_text = font_medium.render(f"Pontuação final: {player.score}", True, WHITE)
    restart = font_medium.render("Pressione ESPAÇO para recomeçar", True, GREEN)

    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//3))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 50))