from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-350, 220)
        self.score = 0
        self.write(f'Score: {self.score}', align='center', font=("Arial", 15, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=("Arial", 15, "normal"))
