import sys
import pygame
from background import Background
from const import WINDOW_MENU_WIDTH, COLOR_WHITE, COLOR_GREEN, COLOR_RED


class Score:
    def __init__(self, window):
        self.window = window

        self.background = Background(name='menu_background/menu', position=(0, 0), isParalax = False) # Carregando tela de fundo

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)

        self.score: int = 0
        self.scores: list[int] = []
        self.fpsValue = None

    def run(self, fpsEnabled: bool) -> None:
        while True:
            self.loadingBackground()  # Limpa a tela e desenha o fundo
            self.fpsValue = str(self.clock.get_fps().__round__(2))  # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais
            self.wrinttingOnTheScreen(fpsEnabled, self.fpsValue)  # Escrevendo na tela

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fechando o jogo
                    pygame.quit()  # Fechando o pygame
                    sys.exit()  # saindo do programa

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:  # Tecla para VOLTAR
                        return  # Sai do loop do run e volta para quem chamou

    def addScore(self, points: int) -> None:
        self.score += points
        self.scores.append(self.score)

    def resetScore(self) -> None:
        self.score = 0

    def getScores(self) -> list[int]:
        return self.scores

    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background.draw(self.window)

    def wrinttingOnTheScreen(self, fpsEnabled: bool, fpsValue: str) -> None:
        if fpsEnabled == True:
            self.draw_text(text = 'FPS: ', text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 80, 20))
            self.draw_text(text = fpsValue, text_color = COLOR_GREEN, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
        else:
            self.draw_text(text = 'FPS: ', text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 80, 20))
            self.draw_text(text = 'OFF', text_color = COLOR_RED, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha()  # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center=text_center_pos)  # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect)  # Desenhando o texto na janela do jogo usando a função blit()