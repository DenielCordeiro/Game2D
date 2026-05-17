import sys
import pygame

from background import Background

from const import (
    COLOR_GREEN,
    COLOR_RED,
    WINDOW_MENU_HEIGHT,
    WINDOW_MENU_WIDTH,
    COLOR_WHITE,
    COMMANDS_TITLE,
    COMMANDS_GAME,
    COMMANDS,
    COMMANDS_RETURN
)

class Commands:
    def __init__(self, window): # inicializando Menu
        self.window = window # Recebendo a janela do jogo para desenhar os comandos
        self.font = pygame.font.SysFont("arial", 20) # Criando fonte para os textos
        self.clock = pygame.time.Clock() # Criando um relógio para controlar a taxa de quadros

    def run(self, fpsEnabled: bool) -> None: # Loop principal do menu de comandos
        while True:
            self.loadingBackground() # Limpa a tela e desenha o fundo
            self.fpsValue = str(self.clock.get_fps().__round__(2)) # Obtendo o valor atual dos FPS e convertendo para string, arredondando para 2 casas decimais
            self.wrintingOnTheScreen(self.fpsValue, fpsEnabled) # Desenha os textos na tela
            
            for event in pygame.event.get():  # Verificando os eventos do jogo
                if event.type == pygame.QUIT: # Fechando o jogo
                    pygame.quit() # Fechando o pygame
                    sys.exit() # saindo do programa
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # Tecla para VOLTAR
                        return # Sai do loop do run e volta para quem chamou

            pygame.display.flip() # Atualiza a tela
            self.clock.tick(60) # Limita a taxa de quadros a 60 FPS

    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background = Background(name = 'menu_background/menu', position = (0, 0), isParalax = False) # Background sem efeito de paralaxe
        self.background.draw(self.window)
        
    def wrintingOnTheScreen(self, fpsValue: str, fpsEnabled: bool) -> None:
        if fpsEnabled == True:
            self.draw_text(text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
            self.draw_text(text = fpsValue,  text_color = COLOR_GREEN, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))
        else:
            self.draw_text(text = 'FPS: ',  text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH - 90, 20))
            self.draw_text(text = 'OFF',  text_color = COLOR_RED, text_center_pos = (WINDOW_MENU_WIDTH - 40, 20))

        self.draw_text(text = COMMANDS_TITLE, text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH / 2, 100))

        for command in range(len(COMMANDS_GAME)): # Percorre todos os comandos do jogo
            self.draw_text(text = COMMANDS_GAME[command], text_color = COLOR_WHITE, text_center_pos = (160, 190 + 30 * command))

        for command in range(len(COMMANDS)): # percorre todos os comandos do menu
            self.draw_text(text = COMMANDS[command], text_color = COLOR_WHITE, text_center_pos = (400, 190 + 30 * command))

        self.draw_text(text = COMMANDS_RETURN, text_color = COLOR_WHITE, text_center_pos = (WINDOW_MENU_WIDTH / 2 + 10, WINDOW_MENU_HEIGHT - 70))

    def draw_text(self, text, text_color, text_center_pos) -> None:
            surf = self.font.render(text, True, text_color).convert_alpha() # Renderizando o texto para uma superfície
            rect = surf.get_rect(center = text_center_pos) # Obtendo o retângulo do texto e definindo sua posição central
            self.window.blit(surf, rect) # Desenhando o texto na janela do jogo usando a função blit()