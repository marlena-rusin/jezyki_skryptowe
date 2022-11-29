class Stats:
    def __init__(self, bulls, cows):
        self.bulls = bulls
        self.cows = cows
        
    def show_score(self):
        return print(f"{self.bulls} Bulls, {self.cows} Cows")