from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, -230)
        self.pendown()
        self.setheading(90)
        self.create_line()

    def create_line(self):
        for _ in range(10):
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)