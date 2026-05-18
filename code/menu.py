import sys
import pygame

from background import Background
from game import Game
from score import Score
from commands import Commands
from settings import Settings

from const import (
    COLOR_GREEN,
    COLOR_RED, 
    COLOR_WHITE,
    WINDOW_MENU_WIDTH, 
    WINDOW_MENU_HEIGHT, 
    MENU_OPTIONS, 
    MENU_TITLE,
)

class Menu:
    def __init__(self): # inicializando Menu
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_MENU_WIDTH, WINDOW_MENU_HEIGHT)) # Criando a janela do jogo com as dimensões definidas
        self.clock = pygame.time.Clock() # Criando um objeto de relógio para controlar a taxa de quadros do jogo
        self.font = pygame.font.SysFont("arial", 20) # Criando um objeto de fonte usando a fonte Arial com tamanho 20

        self.option: int = 0 # Variável para controlar a opção atualmente selecionada no menu, iniciando com a primeira opção (índice 0)
        self.fpsEnabled: bool = False # Variável para controlar se os FPS estão habilitados ou não

        self.loadingBackground() # Carregando tela de fundo
        self.loadCommands = Commands(self.window) # Carregando tela de comandos
        self.game = Game(self.window) # Carregando tela de jogo
        self.loadSettings = Settings(self.window) # Carregando tela de ajustes
        self.loadScores = Score(self.window) # Carregando tela de scores

        self.fpsValue = str(self.clock.get_fps().__round__(2)) # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais

        self.run() # Iniciando o loop principal do menu, passando o estado dos FPS como argumento

    def run(self) -> None: # Carregando tela de fundo
        self.loadCommands.run(self.fpsEnabled) # Carregando tela de comandos

        while True:
            self.loadingBackground() 

            self.fpsValue = str(self.clock.get_fps().__round__(2)) # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais
            self.wrintingOnTheScreen(self.fpsValue, self.fpsEnabled) # Escrevendo na tela

            self.capturingSelectedOption(self.fpsEnabled) # Capturando opção selecionada

            pygame.display.flip() # Atualizamos a tela (importante!)
            self.clock.tick(30) # Limitamos a taxa de quadros a 60 FPS

    def loadingBackground(self) -> None: # Carregando tela de fundo
        self.background = Background(name = 'menu_background/menu', position = (0, 0), isParalax = False) # Criando um objeto de fundo usando a classe Background, com o nome do arquivo de imagem e a posição inicial
        self.background.draw(self.window) # Desenhando o fundo na janela do jogo usando o método draw() da classe Background, passando a janela como argumento

    def wrintingOnTheScreen(self, fpsValue: str, fpsEnabled: bool) -> None: # Escrevendo na tela
        if fpsEnabled == True:
            self.draw_text(text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
            self.draw_text(text = fpsValue,  text_color = COLOR_GREEN, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
        else:
            self.draw_text(text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
            self.draw_text(text = 'OFF',  text_color = COLOR_RED, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
    
        # Adicione um título para o menu se quiser!
        self.draw_text(text = MENU_TITLE, text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH / 2, 100))

        for i in range(len(MENU_OPTIONS)):
            color = COLOR_GREEN if i == self.option else COLOR_WHITE
            self.draw_text(text = MENU_OPTIONS[i], text_color = color, text_center_pos = (WINDOW_MENU_WIDTH / 2, 200 + 40 * i))       

    def capturingSelectedOption(self, fpsEnabled: bool) -> None: # Capturando opção selecionada
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Fechando o jogo
                pygame.quit() # Fechando o pygame
                sys.exit() # saindo do programa

            if event.type == pygame.KEYDOWN: # Capturando opção selecionada
                if event.key == pygame.K_DOWN: # Pressionando seta para baixo
                    if self.option < len(MENU_OPTIONS) - 1:
                        self.option += 1
                    else:
                        self.option = 0
                
                if event.key == pygame.K_UP: # Pressionando seta para cima
                    if self.option > 0:
                        self.option -= 1
                    else:
                        self.option = len(MENU_OPTIONS) - 1

                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # Pressionando enter
                    return self.executingOption(self.option, fpsEnabled)
                        
    def executingOption(self, option: int, fpsEnabled: bool) -> None: # Executando opção selecionada
        match option:
            case 0: # JOGAR
                self.game.run(fpsEnabled) # Iniciando o loop principal do jogo, passando o estado dos FPS como argumento
            case 1: # COMANDOS
                self.loadCommands.run(fpsEnabled)
            case 2: # AJUSTES
                self.fpsEnabled = self.loadSettings.run() # Atualizando o estado dos FPS com base no retorno do menu de ajustes
            case 3: # SCORES
                self.loadScores.run(fpsEnabled)
            case 4: # SAIR
                pygame.quit()
                sys.exit()

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha() # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center = text_center_pos) # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect) # Desenhando o texto na janela do jogo usando a função blit()