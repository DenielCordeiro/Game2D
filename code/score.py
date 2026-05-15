class Score:
    def __init__(self, score: int = 0):
        self.score = score

    def add_score(self, points: int):
        self.score += points

    def reset_score(self):
        self.score = 0

    def get_score(self) -> int:
        return self.score