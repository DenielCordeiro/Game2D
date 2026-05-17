from const import OBSTACLE_HEIGHT, OBSTACLE_WIDTH, WINDOW_GAME_HEIGHT, WINDOW_GAME_WIDTH


class Obstacle:
    def __init__(self):
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.positionX: int = WINDOW_GAME_WIDTH + OBSTACLE_WIDTH
        self.positionY: int = WINDOW_GAME_HEIGHT - 45

    def move(self):
        pass

    def draw(self, window):
        pass