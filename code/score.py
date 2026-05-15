class Score:
    def __init__(self, window):
        self.window = window
        self.score: int = 0
        self.scores: list[int] = []

    def run(self) -> None:
        pass

    def addScore(self, points: int) -> None:
        self.score += points
        self.scores.append(self.score)

    def resetScore(self) -> None:
        self.score = 0

    def getScore(self) -> int:
        return self.score

    def getScores(self) -> list[int]:
        return self.scores