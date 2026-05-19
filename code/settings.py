import sys
import pygame
from background import Background
from const import (
    COLOR_RED,
    COLOR_WHITE,
    COLOR_GREEN,
    WINDOW_MENU_WIDTH,
    SETTINGS_TITLE,
    SETTINGS_RETURN,
    SETTINGS_SHOW_FPS,
    SETTINGS_HIDDEN_FPS,
)

class Settings:
    def __init__(self, window):
        self.window = window

        self.background = Background(name='menu_background/menu', position=(0, 0), isParalax = False)  # Cria o plano de fundo
        self.font = pygame.font.SysFont("arial", 20) # Criando um objeto de fonte usando a fonte Arial com tamanho 20
        self.clock = pygame.time.Clock() # Verifica os FPS

        self.options: tuple = () # Variável para armazenar as opções do menu de ajustes, que serão definidas com base no estado dos FPS
        self.optionsFPSOn = (SETTINGS_SHOW_FPS, SETTINGS_RETURN) # Opções do menu de ajustes quando os FPS estão habilitados
        self.optionsFPSOff = (SETTINGS_HIDDEN_FPS, SETTINGS_RETURN) # Opções do menu de ajustes quando os FPS estão desabilitados
        self.option = 0 # Variável para controlar a opção atualmente selecionada no menu de ajustes, iniciando com a primeira opção (índice 0)

        self.fpsEnabled: bool = False # Variável para controlar se os FPS estão habilitados ou não, iniciando como False (desabilitado)

    def run(self) -> bool:
        while True:
            self.loadingBackground()  # Limpa a tela

            self.fpsEnabled = self.fpsEnabled # Atualiza o estado dos FPS com base no argumento passado para o método run
            self.fpsValue = str(self.clock.get_fps().__round__(2)) # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais
            self.wrintingOnTheScreen(self.fpsEnabled, self.fpsValue) # escreve na tela

            if self.fpsEnabled == True:
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
                        optionReturn = self.executingOption(self.option)

                        if optionReturn == False:
                            pygame.display.flip()
                        else:
                            return self.fpsEnabled

            pygame.display.flip() # Atualiza a tela
            self.clock.tick(30) # Limita o FPS a 30

    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background.draw(self.window)

    def wrintingOnTheScreen(self, fpsEnabled: bool, fpsValue: str) -> None:
        self.draw_text(SETTINGS_TITLE, COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH / 2, 100))

        if fpsEnabled == True:
            for i in range(len(self.optionsFPSOff)):
                color = COLOR_GREEN if i == self.option else COLOR_WHITE
                self.draw_text(text = self.optionsFPSOff[i], text_color =  color, text_center_pos = (WINDOW_MENU_WIDTH / 2, 200 + 40 * i))
                self.draw_text( text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
                self.draw_text( text = fpsValue,  text_color = COLOR_GREEN, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
        else:
            for i in range(len(self.optionsFPSOn)):
                color = COLOR_GREEN if i == self.option else COLOR_WHITE
                self.draw_text(text = self.optionsFPSOn[i],  text_color = color, text_center_pos = (WINDOW_MENU_WIDTH / 2, 200 + 40 * i))
                self.draw_text(text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
                self.draw_text(text = 'OFF',  text_color = COLOR_RED, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
                
    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha()  # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center = text_center_pos)  # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect)  # Desenhando o texto na janela do jogo usando a função blit()

    def executingOption(self, option: int) -> bool:
        match option:
            case 0:
                if (self.options[0] == SETTINGS_SHOW_FPS):
                    self.options = self.optionsFPSOff
                    self.fpsEnabled = False
                else:
                    self.options = self.optionsFPSOn
                    self.fpsEnabled = True

                return False

            case 1:
                return True
