import os
import pygame

from const import (
    OBSTACLE_HEIGHT,
    OBSTACLE_WIDTH,
    WINDOW_GAME_HEIGHT,
    OBSTACLE_SPEED,
)

class Obstacle:
    def __init__(self, startPosition: int):
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.positionY: int = WINDOW_GAME_HEIGHT - (OBSTACLE_HEIGHT + 36)

        self.currentDir: str = os.path.dirname(__file__) # Obtendo o diretório atual do arquivo
        self.imagePath = os.path.join(self.currentDir, '..', 'assets', 'obstacle', 'obstacle.png') # Construindo o caminho para a imagem do obstáculo
        self.surf = pygame.image.load(self.imagePath).convert_alpha() # Carregando a imagem do obstáculo e convertendo para otimização
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height)) # Redimensionando a imagem para as dimensões do obstáculo

        self.rect = pygame.Rect(0, 0, self.width, self.height) # Criando um retângulo para a colisão do obstáculo
        self.reset(startPosition) 

    def reset(self, startPosition: int):
        self.positionX: float = float(startPosition + OBSTACLE_WIDTH) # Posicionando o obstáculo na posição inicial.
        self.passed = False  # Reseta a flag de pontuação para o novo ciclo
        self.rect.topleft = (int(self.positionX), self.positionY) # Atualiza a posição do retângulo de colisão para a nova posição do obstáculo.

    def move(self):
        self.positionX -= OBSTACLE_SPEED  # Mover o obstáculo para a esquerda.
        self.rect.x = int(self.positionX)  # Atualiza a posição X da caixa de colisão.

    def draw(self, window):
        window.blit(self.surf, self.rect) # Desenha o obstáculo na tela.