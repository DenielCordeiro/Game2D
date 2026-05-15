import sys
import pygame

from background import Background

from const import (
    WINDOW_MENU_HEIGHT,
    WINDOW_MENU_WIDTH,
    COLOR_WHITE,
    COMMANDS_TITLE,
    COMMANDS_GAME,
    COMMANDS,
    COMMANDS_RETURN
)

class Commands:
    def __init__(self, window):
        self.window = window # Recebendo a janela do jogo para desenhar os comandos
        self.font = pygame.font.SysFont("arial", 20) # Criando fonte para os textos
        self.clock = pygame.time.Clock() # Criando um relógio para controlar a taxa de quadros

    def run(self):
        while True:
            self.loadingBackground() # Limpa a tela
            self.wrintingOnTheScreen() # Desenha os textos na tela

            # Captura eventos na tela de comandos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Fechando o jogo
                    pygame.quit() # Fechando o pygame
                    sys.exit() # saindo do programa
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # Tecla para VOLTAR
                        return # Sai do loop do run e volta para quem chamou

            pygame.display.flip() # Atualiza a tela
            self.clock.tick(60) # Limita a taxa de quadros a 60 FPS

    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background = Background(name='menu_background/menu', position=(0, 0))
        self.background.draw(self.window)

    def wrintingOnTheScreen(self) -> None:
        self.draw_text(COMMANDS_TITLE, COLOR_WHITE, (WINDOW_MENU_WIDTH / 2, 100))

        for command in range(len(COMMANDS_GAME)): # Percorre todos os comandos do jogo
            self.draw_text(COMMANDS_GAME[command], COLOR_WHITE, (160, 190 + 30 * command))

        for command in range(len(COMMANDS)): # percorre todos os comandos do menu
            self.draw_text(COMMANDS[command], COLOR_WHITE, (400, 190 + 30 * command))

        self.draw_text(COMMANDS_RETURN, COLOR_WHITE, (WINDOW_MENU_WIDTH / 2 + 10, WINDOW_MENU_HEIGHT - 70))

    def draw_text(self, text, color, pos) -> None:
            surf = self.font.render(text, True, color).convert_alpha() # Renderizando o texto para uma superfície
            rect = surf.get_rect(center=pos) # Obtendo o retângulo do texto e definindo sua posição central
            self.window.blit(surf, rect) # Desenhando o texto na janela do jogo usando a função blit()