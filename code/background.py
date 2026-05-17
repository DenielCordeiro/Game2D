from importlib.resources import files
import os
import pygame
from const import (
    BACKGROUND_FOLDER_NAME,
    BACKGROUND_SPEED,
    PLAYER_SPEED, 
    WINDOW_GAME_HEIGHT,
    WINDOW_GAME_WIDTH,
)

class Background:
    def __init__(self, name: str, position: tuple, isParalax: bool):
        self.name = name
        self.position = position
        self.currentDir = os.path.dirname(os.path.abspath(__file__)) # Obtém o diretório atual do arquivo background.py
        self.layers = [] # Lista para armazenar as camadas do plano de fundo
       
        if isParalax == True:  
            self.folder_name = BACKGROUND_FOLDER_NAME #
            self.basePath = os.path.join(self.currentDir, '..', 'assets', 'background', self.folder_name)
            self.loadLayer(self.basePath)

        elif name:
            self.loadImages(name)
            self.rect = self.buildRect(position)


    # Métodos para o plano de fundo estático

    def draw(self, window):
        window.blit(self.surf, self.rect) # desenha a imagem do background na janela do jogo usando o retângulo para posicionamento
    
    def loadImages(self, name: str):
        imagePath = os.path.join(self.currentDir, '..', 'assets', 'background', f'{name}.png') # constrói o caminho completo para a imagem do background
        self.surf = pygame.image.load(imagePath).convert_alpha() # carrega a imagem do background
        self.surf = pygame.transform.scale(self.surf, (WINDOW_GAME_WIDTH, WINDOW_GAME_HEIGHT)) # redimensiona a imagem do background para o tamanho da janela do jogo

    def buildRect(self, position: tuple):
        return self.surf.get_rect(left=position[0], top=position[1]) # cria um retângulo para o background com a posição especificada
    
    # Métodos para o plano de fundo com efeito de paralaxe
    
    def drawingParalax(self, window):
        self.drawParalax(window, PLAYER_SPEED) # Desenha o plano de fundo com efeito de paralaxe

    def loadLayer(self, basePath: str):
        try:
            self.files = sorted([f for f in os.listdir(basePath) if f.lower().endswith('.png')]) # lista e ordena todos os arquivos PNG.
        except FileNotFoundError:
            print(f"Erro: A pasta {basePath} não foi encontrada!")
            return

        for file in self.files:
            imagePath = os.path.join(basePath, file) # Constrói o caminho completo para cada arquivo de imagem
            surf = pygame.image.load(imagePath).convert_alpha() # Carrega a imagem e converte para um formato otimizado para exibição com transparência
            surf = pygame.transform.scale(surf, (WINDOW_GAME_WIDTH, WINDOW_GAME_HEIGHT)) # Redimensiona a imagem para o tamanho da janela do jogo
            
            self.layers.append({'surf': surf, 'x': 0}) # Adiciona a camada à lista de camadas, armazenando a superfície da imagem e a posição x inicial (0)

    def drawParalax(self, window, playerSpeed: float):
        baseSpeed = BACKGROUND_SPEED
        
        for index, layer in enumerate(self.layers):
            layerSpeed = playerSpeed * (baseSpeed * (index + 1)) # Calcula a velocidade da camada com base na velocidade do jogador e na profundidade da camada (camadas mais distantes se movem mais lentamente)
            
            layer['x'] -= layerSpeed # Move a camada para a esquerda com base na velocidade calculada
            
            if layer['x'] <= -WINDOW_GAME_WIDTH: # Se a imagem saiu totalmente da tela pela esquerda, reseta a posição
                layer['x'] = 0

            window.blit(layer['surf'], (layer['x'], 0)) # Desenha a camada na janela do jogo na posição atual
            window.blit(layer['surf'], (layer['x'] + WINDOW_GAME_WIDTH, 0)) # Desenha uma cópia idêntica logo atrás dela para cobrir o espaço em branco