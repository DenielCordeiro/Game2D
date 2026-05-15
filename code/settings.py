import sys
import pygame
from background import Background
from const import COLOR_WHITE, COLOR_GREEN, WINDOW_MENU_WIDTH, WINDOW_MENU_HEIGHT

class Settings:
    def __init__(self, window, fps_enabled: bool):
        self.window = window
        self.font = pygame.font.SysFont("arial", 20)
        self.clock = pygame.time.Clock() # Verifica os FPS
        self.fps_enabled = fps_enabled
        self.option = 0


    def run(self):
        while True:
            self.loadingBackground()  # Limpa a tela
            self.wrintingOnTheScreen() # escreve na tela

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Fechando o jogo
                    pygame.quit()  # Fechando o pygame
                    sys.exit()  # saindo do programa


            pygame.display.flip() # Atualiza a tela
            self.clock.tick(60) # Limita o FPS a 60

    def wrintingOnTheScreen(self) -> None:
        pass


    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background = Background(name = 'menu_background/menu', position=(0, 0))
        self.background.draw(self.window)

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha()  # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center = text_center_pos)  # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect)  # Desenhando o texto na janela do jogo usando a função blit()