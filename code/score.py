import sys
import os
import pygame
from background import Background
from const import WINDOW_MENU_WIDTH, COLOR_WHITE, COLOR_GREEN, COLOR_RED, SCORES_BUTTONS


class Scores:
    def __init__(self, window):
        self.window = window

        self.background = Background(name = 'menu_background/menu', position = (0, 0), isParalax = False) # Carregando tela de fundo

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)

        self.currentDir: str = os.path.dirname(os.path.abspath(__file__)) # Obtendo o diretório atual do arquivo player.py
        self.fileScores = os.path.join(self.currentDir, '..', 'data', 'scores.txt') # Caminho completo para o arquivo de pontuações
        self.scores = self.loadScores() # Carregando as pontuações do arquivo para a lista de pontuações

        self.fpsValue = None
        self.buttonSelected = 0

    def loadScores(self) -> list[int]:
        if not os.path.exists(self.fileScores): # Verificando se o arquivo de pontuações existe
            return []

        try:
            with open(self.fileScores, 'r') as file: # Abrindo o arquivo de pontuações para leitura
                lines = file.readlines() # Lendo todas as linhas do arquivo
                pointsList = [int(line.strip()) for line in lines if line.strip().isdigit()] # Convertendo cada linha em um número inteiro, ignorando linhas vazias.
                pointsList.sort(reverse=True) # Ordenando a lista de pontuações em ordem decrescente.
                pointsList = pointsList[:5] # Mantendo apenas as 5 maiores pontuações.

                return pointsList
            
        except Exception as error:
            print("Erro ao ler arquivo de scores:", error)
            return []

    def run(self, fpsEnabled: bool) -> None:
        self.scores = self.loadScores()
        
        while True:
            self.loadingBackground()  # Limpa a tela e desenha o fundo
            self.fpsValue = str(self.clock.get_fps().__round__(2))  # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais
            self.wrinttingOnTheScreen(fpsEnabled, self.fpsValue)  # Escrevendo na tela

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fechando o jogo
                    pygame.quit()  # Fechando o pygame
                    sys.exit()  # saindo do programa

                if event.type == pygame.KEYDOWN: # Capturando opção selecionada
                    if event.key == pygame.K_UP: # Pressionando seta para cima
                        if self.buttonSelected < len(SCORES_BUTTONS) - 1:
                            self.buttonSelected += 1
                        else:
                            self.buttonSelected = 0
                        
                    if event.key == pygame.K_DOWN: # Pressionando seta para baixo
                        if self.buttonSelected > 0:
                            self.buttonSelected -= 1
                        else:
                            self.buttonSelected = len(SCORES_BUTTONS) - 1

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # Pressionando enter
                        if self.buttonSelected == 0:
                            return
                        elif self.buttonSelected == 1:
                            self.resetScore()
            
            pygame.display.flip()  # Faz os desenhos aparecerem na tela
            self.clock.tick(30)    # Segura a tela em 30 FPS estáveis

    def addScore(self, points: int) -> None:
        if points <= 0:
            return # Se a pontuação for zero ou negativa, não adiciona ao placar
        
        try:
            folderData = os.path.dirname(self.fileScores) # Obtendo o diretório onde o arquivo de pontuações deve estar localizado
             
            if not os.path.exists(folderData): # Verificando se o diretório existe
                os.makedirs(folderData) # Criando o diretório caso ele não exista

            with open(self.fileScores, 'a') as file: # Abrindo o arquivo de pontuações para adicionar a nova pontuação
                file.write(f"{points}\n")
            
            self.scores = self.loadScores() # Recarregando as pontuações para atualizar a lista de pontuações com a nova pontuação adicionada

        except Exception as error:
            print("Erro ao adicionar pontuação:", error)

    def resetScore(self) -> None:
        if os.path.exists(self.fileScores): # Verificando se o arquivo de pontuações existe antes de tentar deletá-lo
            os.remove(self.fileScores)
        
        self.scores = []

    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background.draw(self.window) 

    def getScores(self) -> None:
        if not self.scores:
            self.draw_text(text = "NENHUM RECORDE GRAVADO", text_color = COLOR_RED, text_center_pos = (WINDOW_MENU_WIDTH / 2, 210))
            return

        for i in range(len(self.scores)): # Escreve cada pontuação na tela, formatada como "1º: 100", "2º: 80", etc.
            self.draw_text(text = f'{i + 1}º Lugar: {self.scores[i]} pontos', text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH / 2, 200 + 35 * i))

    def wrinttingOnTheScreen(self, fpsEnabled: bool, fpsValue: str) -> None:
        if fpsEnabled == True:
            self.draw_text(text = 'FPS: ', text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
            self.draw_text(text = fpsValue, text_color = COLOR_GREEN, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
        else:
            self.draw_text(text = 'FPS: ', text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
            self.draw_text(text = 'OFF', text_color = COLOR_RED, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))

        self.getScores()

        for i in range(len(SCORES_BUTTONS)):
            color = COLOR_GREEN if i == self.buttonSelected else COLOR_WHITE
            self.draw_text(text = SCORES_BUTTONS[i], text_color = color, text_center_pos = (WINDOW_MENU_WIDTH / 2, 90 + 40 * i))

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha()  # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center=text_center_pos)  # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect)  # Desenhando o texto na janela do jogo usando a função blit()