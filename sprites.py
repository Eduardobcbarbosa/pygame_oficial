import pygame
import random
from config import WIDTH, HEIGHT, BLUE, WHITE, YELLOW, RED, PURPLE, BLACK

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = WIDTH - 100
        self.y = HEIGHT // 2
        self.speed = 5
        self.lives = 3
        self.score = 0
        
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    def move(self, keys):
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed
            
    def shoot(self, bullets):
        bullets.append(Bullet(self.x - 20, self.y + self.height//2))
        

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.width = 5
        self.height = 5
        
    def update(self):
        self.x -= self.speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        
    def is_off_screen(self):
        return self.x < 0

class Enemy:
    def __init__(self, speed):
        self.width = 40
        self.height = 40
        self.x = 0
        self.y = random.randint(0, HEIGHT - self.height)
        self.speed = speed
        self.word = "DP"
        
    def update(self):
        self.x += self.speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(self.word, True, WHITE)
        screen.blit(text, (self.x + 10, self.y + 10))
        
    def is_past_line(self):
        return self.x > WIDTH - 150

class QuizWord:
    def __init__(self, speed):
        self.width = 60
        self.height = 40
        self.x = 0
        self.y = random.randint(0, HEIGHT - self.height)
        self.speed = speed
        self.word = "QUIZ"
        
    def update(self):
        self.x += self.speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, PURPLE, (self.x, self.y, self.width, self.height))
        text = pygame.font.SysFont('Arial', 20).render(self.word, True, WHITE)
        screen.blit(text, (self.x + 5, self.y + 10))
        
    def is_past_line(self):
        return self.x > WIDTH - 150

class Heart:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = random.randint(50, WIDTH - 200)
        self.y = random.randint(50, HEIGHT - 50)
        self.speed = 3
        self.active = False
        
    def update(self):
        if self.active:
            self.x += self.speed
        
    def draw(self, screen):
        if self.active:
           # raio dos círculos e o tamanho do triângulo
            radius = self.width // 4
            
            # Posições dos centros dos círculos
            circle1_x = self.x + radius
            circle1_y = self.y + radius
            circle2_x = self.x + self.width - radius
            circle2_y = self.y + radius

            # Pontos do triângulo
            triangle_point_top = (self.x + self.width // 2, self.y + self.height // 3) # Ajustado para a ponta do coração
            triangle_point_left = (self.x, self.y + self.height // 3) # Aproximadamente na base dos círculos
            triangle_point_right = (self.x + self.width, self.y + self.height // 3) # Aproximadamente na base dos círculos
            triangle_point_bottom = (self.x + self.width // 2, self.y + self.height)


            # dois círculos superiores
            pygame.draw.circle(screen, RED, (circle1_x, circle1_y), radius)
            pygame.draw.circle(screen, RED, (circle2_x, circle2_y), radius)

            # Desenha o triângulo que forma a parte inferior do coração
            pygame.draw.polygon(screen, RED, [
                (self.x + self.width // 2, self.y + radius * 2),  # Ponto central abaixo dos círculos
                (self.x, self.y + self.height * 0.7),  # Ponto esquerdo da parte de baixo do coração
                (self.x + self.width // 2, self.y + self.height), # Ponto da ponta inferior do coração
                (self.x + self.width, self.y + self.height * 0.7)  # Ponto direito da parte de baixo do coração
            ])
           # Uma forma alternativa e mais precisa para a parte inferior
            # Você pode preencher um polígono que conecta os círculos e a ponta
            pygame.draw.polygon(screen, RED, [
                (self.x + self.width // 2, self.y + self.height), # Ponta inferior
                (self.x, self.y + self.height // 3), # Ponto inferior esquerdo do círculo esquerdo
                (self.x + self.width // 2, self.y + radius), # Ponto de conexão entre os círculos
                (self.x + self.width, self.y + self.height // 3) # Ponto inferior direito do círculo direito
            ])
            
    def is_past_line(self):
        return self.x > WIDTH - 150