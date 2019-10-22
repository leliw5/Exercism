class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        self.scores.sort()
        return self.scores[-1]

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        self.scores.sort(reverse=True)
        return self.scores[:3]