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
        self.positionX: int = startPosition + OBSTACLE_WIDTH
        self.positionY: int = WINDOW_GAME_HEIGHT - (OBSTACLE_HEIGHT + 36)

        self.rect = pygame.Rect(self.positionX, self.positionY, self.width, self.height) # caixa de colisão do obstáculo.
        self.passed = False # veriricar se o obstáculo já passou do jogador para pontuação.

        self.currentDir: str = os.path.dirname(__file__)
        self.imagePath = os.path.join(self.currentDir, '..', 'assets', 'obstacle', 'obstacle.png')
        self.surf = pygame.image.load(self.imagePath).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))

    def move(self):
        self.positionX -= OBSTACLE_SPEED # mover o obstáculo para a esquerda.
        self.rect.topleft = (self.positionX, self.positionY) # atualizar a posição da caixa de colisão do obstáculo.

    def draw(self, window):
        window.blit(self.surf, self.rect)