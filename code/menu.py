import sys
import pygame

from background import Background
from score import Score
from commands import Commands
from settings import Settings

from const import COLOR_GREEN, COLOR_WHITE, WINDOW_MENU_WIDTH, WINDOW_MENU_HEIGHT, MENU_OPTIONS, MENU_TITLE

class Menu:
    def __init__(self): # inicializando Menu
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_MENU_WIDTH, WINDOW_MENU_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.option: int = 0
        self.fps_enabled: bool = False

        self.loadingBackground()
        self.loadCommands = Commands(self.window)
        self.loadSettings = Settings(self.window, self.fps_enabled)
        self.loadScores = Score(self.window)

        self.startingGame()


    def startingGame(self) -> None: # Carregando tela de fundo
        self.loadCommands.run()

        while True:
            self.loadingBackground() 
            self.wrintingOnTheScreen() 
            self.capturingSelectedOption()

            pygame.display.flip() # Atualizamos a tela (importante!)
            self.clock.tick(60) # Limitamos a taxa de quadros a 60 FPS

    def loadingBackground(self) -> None: # Carregando tela de fundo
        self.background = Background(name = 'menu_background/menu', position = (0, 0))
        self.background.draw(self.window)


    def wrintingOnTheScreen(self) -> None: # Escrevendo na tela
        # Adicione um título para o menu se quiser!
        self.draw_text(MENU_TITLE, COLOR_WHITE, (WINDOW_MENU_WIDTH / 2, 100))

        for i in range(len(MENU_OPTIONS)):
            color = COLOR_GREEN if i == self.option else COLOR_WHITE
            self.draw_text(MENU_OPTIONS[i], color, (WINDOW_MENU_WIDTH / 2, 200 + 40 * i))

    def capturingSelectedOption(self) -> None: # Capturando opção selecionada
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
                    return self.executingOption(self.option)
                        
    def executingOption(self, option: int) -> None: # Executando opção selecionada
        match option:
            case 0: # JOGAR
                print('Exibindo os Jogo...')
            case 1: # COMANDOS
                self.loadCommands.run()
            case 2: # AJUSTES
                self.loadSettings.run()
            case 3: # SCORES
                self.loadScores.run()
            case 4: # SAIR
                pygame.quit()
                sys.exit()

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha() # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center=text_center_pos) # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect) # Desenhando o texto na janela do jogo usando a função blit()