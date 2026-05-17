import sys
import pygame

from background import Background
from obstacle import Obstacle
from player import Player
from const import (
    COLOR_GREEN,
    COLOR_RED,
    COLOR_WHITE,
    WINDOW_MENU_WIDTH,
)

class Game:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont("arial", 14) # Criando um objeto de fonte usando a fonte Arial com tamanho 20. 
        self.clock = pygame.time.Clock() # Criando um objeto de relógio para controlar a taxa de quadros do jogo.

        self.backgroundParalax = Background(name='game_background', position=(0, 0), isParalax = True) # importando o fundo do jogo.
        self.obstacle = Obstacle(startPosition = WINDOW_MENU_WIDTH) # Criando um obstáculo na posição y=380.
        self.player = Player() # Criando o player.

    def run(self, fpsEnabled: bool) -> None:
        while True:
            self.fpsValue = str(self.clock.get_fps().__round__(2)) # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais
            self.loadingBackground()

            self.obstacle.move() # Movimento do obstáculo
            self.obstacle.draw(self.window) # Desenhando obstáculo.

            self.player.move() # Movimento do player
            self.player.draw(self.window) # Desenhando player.

            self.checkingCollision() # Verificando colisão entre player e obstáculo.

            self.wrinttingOnTheScreen(fpsEnabled, self.fpsValue) # escreve na tela

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fechando o jogo
                    pygame.quit()  # Fechando o pygame
                    sys.exit()  # saindo do programa

                if event.type == pygame.KEYDOWN: # Capturando opção selecionada
                    if event.key == pygame.K_SPACE: # Se pressionar ESPAÇO, o player pula
                        self.player.jump()
                        
                    if event.key == pygame.K_ESCAPE:
                        return
                    
            pygame.display.flip() # Atualiza a tela
            self.clock.tick(60) # Limita a taxa de quadros a 60 FPS

    def loadingBackground(self) -> None:
        self.backgroundParalax.drawingParalax(self.window) # Desenhando o fundo com efeito de paralaxe na janela do jogo.

    def checkingCollision(self) -> None:
        if self.player.rect.colliderect(self.obstacle.rect): # Verificando se o retângulo do player colidiu com o retângulo do obstáculo.
            print(f"GAME OVER! Pontuação final: {self.score}")
            
        if self.player.positionX > self.obstacle.positionX and not self.obstacle.passed: # Verificando se o player passou do obstáculo.
            self.score += 10
            self.obstacle.passed = True 
            
        if self.obstacle.positionX < -self.obstacle.width: # Verificando se o obstáculo saiu completamente da tela.
            self.obstacle = Obstacle(startPosition = WINDOW_MENU_WIDTH) 

    def wrinttingOnTheScreen(self, fpsEnabled: bool, fpsValue: str) -> None:
        if fpsEnabled == True:
            self.draw_text(text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 80, 20))
            self.draw_text(text = fpsValue,  text_color = COLOR_GREEN, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
        else:
            self.draw_text(text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 80, 20))
            self.draw_text(text = 'OFF',  text_color = COLOR_RED, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)