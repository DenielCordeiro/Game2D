import pygame
from const import WINDOW_GAME_HEIGHT, WINDOW_GAME_WIDTH

class Background:
    def __init__(self, name: str, position: tuple):
        self.loadImages(name)
        self.rect = self.buildRect(position)

    def loadImages(self, name: str):
        self.surf = pygame.image.load('../assets/background/' + name + '.png').convert_alpha() # carrega a imagem do background
        self.surf = pygame.transform.scale(self.surf, (WINDOW_GAME_WIDTH, WINDOW_GAME_HEIGHT)) # redimensiona a imagem do background para o tamanho da janela do jogo


    def buildRect(self, position: tuple):
        return self.surf.get_rect(left=position[0], top=position[1]) # cria um retângulo para o background com a posição especificada

    def draw(self, window):
        window.blit(self.surf, self.rect)