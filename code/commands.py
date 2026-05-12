import sys
import pygame
from pygame import Surface


class Commands:
    def __init__(self, window: Surface):
        self.window = window # Recebendo a janela do jogo para desenhar os comandos
        self.font = pygame.font.SysFont("arial", 20) # Criando fonte para os textos
        self.clock = pygame.time.Clock() # Criando um relógio para controlar a taxa de quadros

    def run(self):
        while True:
            self.window.fill((0, 0, 0)) # Limpa a tela

            self.wrintingOnTheScreen()

            # Captura eventos na tela de comandos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Fechando o jogo
                    pygame.quit() # Fechando o pygame
                    sys.exit() # saindo do programa
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Tecla para VOLTAR
                        return # Sai do loop do run e volta para quem chamou

            pygame.display.flip() # Atualiza a tela
            self.clock.tick(60) # Limita a taxa de quadros a 60 FPS

    def wrintingOnTheScreen(self):
        self.draw_text("Comandos", (255, 255, 0), (290, 100))

        self.draw_text("Menu:", (255, 255, 255), (450, 200))
        self.draw_text("Seta para Cima - Cima", (255, 255, 255), (450, 230))
        self.draw_text("Seta para Baixo - Baixo", (255, 255, 255), (450, 260))
        self.draw_text("Enter - Selecionar", (255, 255, 255), (450, 290))

        self.draw_text("Jogo:", (255, 255, 255), (150, 200))
        self.draw_text("space - Pular", (255, 255, 255), (150, 230))

    def draw_text(self, text, color, pos):
        surf = self.font.render(text, True, color).convert_alpha() # Renderizando o texto para uma superfície
        rect = surf.get_rect(center=pos) # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(surf, rect) # Desenhando o texto na janela do jogo usando a função blit()