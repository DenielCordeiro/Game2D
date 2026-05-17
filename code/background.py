import os
from turtle import position
import pygame
from const import WINDOW_GAME_HEIGHT, WINDOW_GAME_WIDTH

class Background:
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position

    def loadImages(self, name: str):
        current_dir = os.path.dirname(__file__) # obtém o diretório atual do arquivo background.py
        image_path = os.path.join(current_dir, '..', 'assets', 'background', f'{name}.png') # constrói o caminho completo para a imagem do background
        self.surf = pygame.image.load(image_path).convert_alpha() # carrega a imagem do background
        self.surf = pygame.transform.scale(self.surf, (WINDOW_GAME_WIDTH, WINDOW_GAME_HEIGHT)) # redimensiona a imagem do background para o tamanho da janela do jogo

    def buildRect(self, position: tuple):
        return self.surf.get_rect(left=position[0], top=position[1]) # cria um retângulo para o background com a posição especificada

    def draw(self, window):
        self.loadImages(self.name) # carrega a imagem do background
        self.rect = self.buildRect(self.position) # constrói o retângulo para o background

        window.blit(self.surf, self.rect) # desenha a imagem do background na janela do jogo usando o retângulo para posicionamento
    
    def drawParalax(self):
        pass