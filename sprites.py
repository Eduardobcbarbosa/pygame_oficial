import pygame
import random
from config import WIDTH, HEIGHT, BLUE, WHITE, YELLOW, RED, PURPLE, BLACK

class Player:
    def __init__(self):
        # config iniciais jogador
        self.width = 50 # largura sprite
        self.height = 50 # altura sprite 
        self.x = WIDTH - 100 # posicao x inicial
        self.y = HEIGHT // 2 # posicao y inicial
        self.speed = 5 # velocidade movimento
        self.lives = 3 # vidas iniciais
        self.score = 0 # pontuacao inicial
        # carrega e redimensiona imagem jogador 
        self.image = pygame.image.load('assets/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    #desenha jogador    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    #move jogador 
    def move(self, keys):
        if keys[pygame.K_UP] and self.y > 0: # move para cima
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height: # move para baixo
            self.y += self.speed
            
    def shoot(self, bullets):
        bullets.append(Bullet(self.x - 20, self.y + self.height//2))
        

class Bullet:
    def __init__(self, x, y):
        #configs iniciais bala
        self.x = x #posicao x inciial
        self.y = y # posicao y inicial
        self.speed = 10 # velocidade bala
        self.width = 5 # largura
        self.height = 5 # altura 
        
    #posição
    def update(self):
        self.x -= self.speed

    #desenha bala    
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
    #define momento em que a bala sai da tela   
    def is_off_screen(self):
        return self.x < 0

class Enemy:
    def __init__(self, speed):
        # configurações iniciais inimigo
        self.width = 40 #largura
        self.height = 40 # altura
        self.x = 0 #posicao x inicial
        self.y = random.randint(0, HEIGHT - self.height) # posicao y aleatoria
        self.speed = speed # velocidade
        self.word = "DP" #texto inimigo
    #posição   
    def update(self):
        self.x += self.speed
    #desenha inimigo    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(self.word, True, WHITE)
        screen.blit(text, (self.x + 10, self.y + 10))
    #define quando sai da tela    
    def is_past_line(self):
        return self.x > WIDTH - 150

class QuizWord:
    def __init__(self, speed):
        # configs iniciais
        self.width = 60 # largura maior pro texto
        self.height = 40 #altura
        self.x = 0 # posicao x inicial
        self.y = random.randint(0, HEIGHT - self.height) # posicao y aleatoria
        self.speed = speed #velocidade
        self.word = "QUIZ" # texto fixo
    #posição   
    def update(self):
        self.x += self.speed
    #desenha quiz   
    def draw(self, screen):
        pygame.draw.rect(screen, PURPLE, (self.x, self.y, self.width, self.height))
        text = pygame.font.SysFont('Arial', 20).render(self.word, True, WHITE)
        screen.blit(text, (self.x + 5, self.y + 10))
    #define quando sai da tela   
    def is_past_line(self):
        return self.x > WIDTH - 150

class Heart:
    def __init__(self):
        # configs inciais 
        self.width = 30 # largura
        self.height = 30 # altura
        self.x = random.randint(50, WIDTH - 200) # posicao x aleatoria
        self.y = random.randint(50, HEIGHT - 50) # posicao y aleatoria
        self.speed = 3 # velocidade
        self.active = False # estado inicial (inativo)
    #posição quando tiver ativo    
    def update(self):
        if self.active:
            self.x += self.speed
    #desenha coração    
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
    #define quando sai da tela        
    def is_past_line(self):
        return self.x > WIDTH - 150