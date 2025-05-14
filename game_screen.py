import pygame
from config import screen, font_xl, font_medium, font_large, WHITE, RED, GREEN
from assets import fundodetela_menu, fundodetela_game_over

def draw_menu():
    screen.blit(fundodetela_menu, (0, 0))
    title = font_xl.render("Guerra contra a DP", True, WHITE)
    start = font_medium.render("Pressione 'ESPAÇO' para começar", True, RED)
    screen.blit(title, (400 - title.get_width() // 2, 150))
    screen.blit(start, (400 - start.get_width() // 2, 300))

def draw_game_over(player):
    screen.blit(fundodetela_game_over, (0, 0))
    text = font_large.render("GAME OVER", True, RED)
    score_text = font_medium.render(f"Pontuação: {player.score}", True, WHITE)
    restart = font_medium.render("Pressione ESPAÇO para recomeçar", True, GREEN)

    screen.blit(text, (400 - text.get_width() // 2, 200))
    screen.blit(score_text, (400 - score_text.get_width() // 2, 300))
    screen.blit(restart, (400 - restart.get_width() // 2, 350))