import pygame

from background import Background
from const import COLOR_GREEN, COLOR_RED, COLOR_WHITE, WINDOW_MENU_WIDTH

class Game:
    def __init__(self, window):
        self.window = window

        self.font = pygame.font.SysFont("arial", 20) # Criando um objeto de fonte usando a fonte Arial com tamanho 20  

    def run(self, fpsEnabled: bool) -> None:
        self.fpsValue = str(self.clock.get_fps().__round__(2)) # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais
        self.wrintingOnTheScreen(fpsEnabled, self.fpsValue) # escreve na tela

    def loadingBackground(self):
        self.background = Background(self.window) # Criando uma instância da classe Background, passando a janela do jogo como argumento
        self.background.drawParalax() # Chamando o método draw da instância de Background para desenhar o plano de fundo na janela do jogo

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