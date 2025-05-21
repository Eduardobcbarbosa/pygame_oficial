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
            pygame.draw.polygon(screen, RED, [
                (self.x + self.width//2, self.y),
                (self.x + self.width, self.y + self.height//3),
                (self.x + self.width, self.y + self.height),
                (self.x + self.width//2, self.y + self.height*2//3),
                (self.x, self.y + self.height),
                (self.x, self.y + self.height//3)
            ])
        
    def is_past_line(self):
        return self.x > WIDTH - 150