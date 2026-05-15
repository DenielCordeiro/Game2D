from background import Background


class Settings:
    def __init__(self, window):
        self.window = window

    def run(self):
        while True:
            self.loadingBackground()  # Limpa a tela

    def loadingBackground(self) -> None:  # Carregando tela de fundo
        self.background = Background(name = 'menu_background/menu', position=(0, 0))
        self.background.draw(self.window)

    def draw_text(self, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_surf = self.font.render(text, True, text_color).convert_alpha()  # Renderizando o texto para uma superfície
        text_rect = text_surf.get_rect(center = text_center_pos)  # Obtendo o retângulo do texto e definindo sua posição central
        self.window.blit(text_surf, text_rect)  # Desenhando o texto na janela do jogo usando a função blit()