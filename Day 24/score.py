from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.write(f"Your Score {self.score} High Score: {self.high_score}", move=False, align='center', font=('Arial', 15, 'normal'))


    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", move=False, align='center', font=('Arial', 30, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Your Score {self.score} High Score: {self.high_score}", move=False, align='center', font=('Arial', 15, 'normal'))

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Your Score {self.score} High Score: {self.high_score}", move=False, align='center', font=('Arial', 15, 'normal'))
