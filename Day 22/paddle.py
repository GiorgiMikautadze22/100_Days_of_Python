from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(3, 1)
        self.penup()
        self.goto(-350, 0)


    def up(self):
        self.setheading(90)
        self.forward(10)
        print(self.heading())

    def down(self):
        self.setheading(270)
        self.forward(10)
        print(self.heading())

