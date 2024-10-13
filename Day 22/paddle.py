from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen, position):
        super().__init__()
        self.position = position
        self.player()
        self.screen = screen

    def player(self):
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(-350 * self.position, 0)


    def up(self):
        if self.ycor() < 210:
            self.sety(self.ycor() + 20)


    def down(self):
        if self.ycor() > -210:
            self.sety(self.ycor() - 20)

