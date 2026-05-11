class Menu:
    def __init__(self): # inicializando Menu
        self.loadingBackground()
        self.wrintingOnTheScreen()
        self.capturingSelectedOption()
        pass

    def loadingBackground(self): # Carregando tela de fundo
        pass

    def wrintingOnTheScreen(self): # Escrevendo na tela
        pass

    def capturingSelectedOption(self): # Capturando opção selecionada
        self.executingOption('teste')
        pass

    def executingOption(self, option: str): # Executando opção selecionada
        print(option)
        pass