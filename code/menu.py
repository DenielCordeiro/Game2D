import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from const import COLOR_GREEN, COLOR_WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS, MENU_TITLE

from commands import Commands

class Menu:
    def __init__(self): # inicializando Menu
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.option = 0

        self.loadCommands = Commands(self.window)
        self.startingGame()    


    def startingGame(self): # Carregando tela de fundo  
        self.loadCommands.run()


        while True:
            
            self.window.fill((0, 0, 0)) # Limpa a tela

            self.loadingBackground() 
            self.wrintingOnTheScreen() 
            self.capturingSelectedOption()

            pygame.display.flip() # Atualizamos a tela (importante!)
            self.clock.tick(60) # Limitamos a taxa de quadros a 60 FPS

    def loadingBackground(self): # Carregando tela de fundo
        pass

    def wrintingOnTheScreen(self): # Escrevendo na tela
        # Adicione um título para o menu se quiser!
        self.draw_text(MENU_TITLE, COLOR_WHITE, (WINDOW_WIDTH / 2, 100))

        for i in range(len(MENU_OPTIONS)):
            color = COLOR_GREEN if i == self.option else COLOR_WHITE
            self.draw_text(MENU_OPTIONS[i], color, (WINDOW_WIDTH / 2, 250 + 40 * i))

    def capturingSelectedOption(self): # Capturando opção selecionada
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

                if event.key == pygame.K_RETURN: # Pressionando enter
                    return self.executingOption(self.option)
                        
    def executingOption(self, option: int): # Executando opção selecionada
        match option:
            case 0: # JOGAR
                print('Iniciando o jogo...')
            case 1: # COMANDOS
                self.loadCommands.run()
            case 2: # AJUSTES
                print('Exibindo os ajustes...')
            case 3: # SCORES
                print('Exibindo os scores...')
            case 4: # SAIR
                print('Saindo do jogo...')
                pygame.quit()
                sys.exit()

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple):
        text_surf = self.font.render(text, True, text_color).convert_alpha() # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center=text_center_pos) # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect) # Desenhando o texto na janela do jogo usando a função blit()