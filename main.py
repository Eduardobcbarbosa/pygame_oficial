import pygame
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guerra contra a DP")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MENU = 0
PHASE1 = 1
PHASE2 = 2
GAME_OVER = 3
game_state = MENU

assets = {
    "FASE1_IMG": pygame.image.load('assets/tela_phase1.png'),
    "FASE2_IMG": pygame.image.load('assets/tela_phase2.png'),
    "MENU_IMG": pygame.image.load('assets/tela_inicial.png'),
    "GAME_OVER_IMG": pygame.image.load('assets/tela_game_over.png')
}

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def reset_position(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

def draw_menu():
    screen.blit(assets["MENU_IMG"], (0, 0))

def draw_game_over():
    screen.blit(assets["GAME_OVER_IMG"], (0, 0))

def draw_phase1():
    screen.blit(assets["FASE1_IMG"], (0, 0))
    all_sprites.draw(screen)

def draw_phase2():
    screen.blit(assets["FASE2_IMG"], (0, 0))
    all_sprites.draw(screen)

obstacle = pygame.Rect(200, 150, 100, 100)
portal_to_phase2 = pygame.Rect(600, 500, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                if game_state == MENU:
                    game_state = PHASE1
                    player.reset_position()
                elif game_state == GAME_OVER:
                    game_state = MENU

            if event.key == pygame.K_r and game_state == GAME_OVER:
                game_state = PHASE1
                player.reset_position()

            if event.key == pygame.K_m and game_state == GAME_OVER:
                game_state = MENU

    if game_state == MENU:
        draw_menu()
    elif game_state == GAME_OVER:
        draw_game_over()
    elif game_state == PHASE1:
        all_sprites.update()
        draw_phase1()
        pygame.draw.rect(screen, (255, 0, 0), obstacle)
        pygame.draw.rect(screen, (0, 0, 255), portal_to_phase2)

        if player.rect.colliderect(obstacle):
            game_state = GAME_OVER

        if player.rect.colliderect(portal_to_phase2):
            game_state = PHASE2
    elif game_state == PHASE2:
        all_sprites.update()
        draw_phase2()

    pygame.display.flip()

pygame.quit()
sys.exit()
