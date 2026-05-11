import pygame
import sys
from const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS

class Menu:
    def __init__(self): # inicializando Menu
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.option = 0
        self.startingGame()    

    def startingGame(self): # Carregando tela de fundo        
        while True:
            self.loadingBackground() 
            self.wrintingOnTheScreen()
            self.capturingSelectedOption()
            
            pygame.display.flip() # Atualizamos a tela (importante!)

    def loadingBackground(self): # Carregando tela de fundo
        pass

    def wrintingOnTheScreen(self): # Escrevendo na tela
        pass

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
                print('Exibindo os comandos...')
            case 2: # AJUSTES
                print('Exibindo os ajustes...')
            case 3: # SCORES
                print('Exibindo os scores...')
            case 4: # SAIR
                print('Saindo do jogo...')
                pygame.quit()
                sys.exit()