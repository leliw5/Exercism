class HighScores:
    def __init__(self, scores: list) -> None:
        self.scores = scores

    def personal_best(self) -> int:
        self.scores.sort()
        return self.scores[-1]

    def latest(self) -> int:
        return self.scores[-1]

    def personal_top_three(self) -> list:
        self.scores.sort(reverse=True)
        return self.scores[:3]
