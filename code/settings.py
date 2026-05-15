import sys
import pygame
from background import Background
from const import (
    COLOR_WHITE,
    COLOR_GREEN,
    WINDOW_MENU_WIDTH,
    WINDOW_MENU_HEIGHT,
    SETTINGS_TITLE,
    SETTINGS_RETURN,
    SETTINGS_SHOW_FPS,
    SETTINGS_HIDDEN_FPS,
    SETTINGS_STATUS_ON ,
    SETTINGS_STATUS_OFF
)

class Settings:
    def __init__(self, window, fps_enabled: bool):
        self.window = window
        self.font = pygame.font.SysFont("arial", 20)
        self.clock = pygame.time.Clock() # Verifica os FPS
        self.fps_enabled = fps_enabled
        self.option = 0
        self.optionsFPSOn = (SETTINGS_SHOW_FPS, SETTINGS_RETURN)
        self.optionsFPSOff = (SETTINGS_HIDDEN_FPS, SETTINGS_RETURN)
        self.options: tuple = ()

    def run(self):
        while True:
            self.loadingBackground()  # Limpa a tela
            self.wrintingOnTheScreen() # escreve na tela

            if self.fps_enabled == True:
                self.options = self.optionsFPSOn
            else:
                self.options = self.optionsFPSOff

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fechando o jogo
                    pygame.quit()  # Fechando o pygame
                    sys.exit()  # saindo do programa

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Pressionando seta para baixo
                        if self.option < len(self.options) - 1:
                            self.option += 1
                        else:
                            self.option = 0

                    if event.key == pygame.K_UP:  # Pressionando seta para cima
                        if self.option > 0:
                            self.option -= 1
                        else:
                            self.option = len(self.options) - 1

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:  # Pressionando enter
                        return self.executingOption(self.option)

            pygame.display.flip() # Atualiza a tela
            self.clock.tick(60) # Limita o FPS a 60

    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background = Background(name = 'menu_background/menu', position=(0, 0))
        self.background.draw(self.window)

    def wrintingOnTheScreen(self) -> None:
        self.draw_text(SETTINGS_TITLE, COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH / 2, 100))

        if self.fps_enabled == True:
            for i in range(len(self.optionsFPSOff)):
                color = COLOR_GREEN if i == self.option else COLOR_WHITE
                self.draw_text(self.optionsFPSOff[i], color, text_center_pos = (WINDOW_MENU_WIDTH / 2, 200 + 40 * i))
        else:
            for i in range(len(self.optionsFPSOn)):
                color = COLOR_GREEN if i == self.option else COLOR_WHITE
                self.draw_text(self.optionsFPSOn[i], color, text_center_pos = (WINDOW_MENU_WIDTH / 2, 200 + 40 * i))

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha()  # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center = text_center_pos)  # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect)  # Desenhando o texto na janela do jogo usando a função blit()

    def executingOption(self, option: int) -> None:
        match option:
            case 0:
                print('Opção escolhida: ', self.optionsFPSOn[option])
                return
            case 1:
                print('Opção escolhida: ', self.optionsFPSOn[option])
                return