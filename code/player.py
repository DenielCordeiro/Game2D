import os
import pygame
from const import  (
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    WINDOW_GAME_HEIGHT,
)

class Player:
    def __init__(self):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.positionX = 25 # Posição inicial do player em relação ao eixo x
        self.positionY = WINDOW_GAME_HEIGHT - self.height - 30 # Posição do chão 
        self.lastPosition = self.positionY

        self.rect = pygame.Rect(self.positionX, self.lastPosition, self.width, self.height) # Para checar se o player está no chão ou no ar, e colisões com objetos.

        self.speedJump = 0 # Velocidade vertical do player, que é afetada pela gravidade e pela força do pulo.
        self.gravidade = 0.8 # Força que puxa o player para baixo a cada frame
        self.jumpForce = -15 # Força inicial do pulo 
        self.isJump = False # Garante que ele não pule no ar (anula pulo duplo)

        currentDir = os.path.dirname(os.path.abspath(__file__)) # Obtendo o diretório atual do arquivo player.py
        imagePath = os.path.join(currentDir, '..', 'assets', 'player', 'player.png') # Caminho para imagem do player.
        self.surf = pygame.image.load(imagePath).convert_alpha() # carregando a imagem do player e convertendo para um formato otimizado.
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))  # Redimensionando a imagem do player.

    def jump(self):
        if not self.isJump: # Verifica se o player não está pulando no momento
            self.speedJump = self.jumpForce
            self.isJump = True
        else:
            pass # Se o player já estiver pulando, não faz nada (impede pulo duplo)

    def move(self):
        self.speedJump += self.gravidade # Aplica a gravidade à velocidade de pulo, fazendo o player cair mais rápido com o tempo
        self.lastPosition += self.speedJump # Atualiza a posição vertical do player com base na velocidade de pulo, fazendo ele subir ou descer dependendo do valor de speedJump

        if self.lastPosition >= self.positionY: # Verifica se o player atingiu ou ultrapassou a posição do chão
            self.lastPosition = self.positionY # Garante que o player não caia abaixo do chão, corrigindo a posição para a altura do chão
            self.speedJump = 0
            self.isJump = False # Libera para pular de novo
        else:
            pass # Se o player ainda estiver no ar, não faz nada

        self.rect.topleft = (self.positionX, self.lastPosition) # Atualiza a posição de colisão do player para corresponder à nova posição

    def draw(self, window):
        window.blit(self.surf, self.rect) # Desenha o player na tela.