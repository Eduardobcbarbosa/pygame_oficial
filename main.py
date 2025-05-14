import pygame
import sys
from config import *

running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BLACK)
    pygame.display.flip()

pygame.quit()
sys.exit()
