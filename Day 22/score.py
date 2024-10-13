from turtle import Turtle

class Score(Turtle):
    def __init__(self, ):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 150)


    def show_score(self):
        self.clear()
        self.write(f'{self.score_1}  {self.score_2}', align='center', font=("Arial", 40, "normal"))
