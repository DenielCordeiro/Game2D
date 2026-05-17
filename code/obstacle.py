import pygame

from const import (
    COLOR_YELLOW,
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
        self.positionY: int = WINDOW_GAME_HEIGHT - 45

        self.rect = pygame.Rect(self.positionX, self.positionY, self.width, self.height) # caixa de colisão do obstáculo.
        self.passed = False # veriricar se o obstáculo já passou do jogador para pontuação.
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(COLOR_YELLOW)

    def move(self):
        self.positionX -= OBSTACLE_SPEED # mover o obstáculo para a esquerda.
        self.rect.topleft = (self.positionX, self.positionY) # atualizar a posição da caixa de colisão do obstáculo.

    def draw(self, window):
        window.blit(self.surf, self.rect)