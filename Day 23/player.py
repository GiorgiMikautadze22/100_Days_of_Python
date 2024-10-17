from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.x_cor = 0
        self.y_cor = 0
        self.refresh()

    def up(self):
        self.y_cor += 10
        self.goto(self.x_cor,self.y_cor)
        self.setheading(90)

    def down(self):
        self.y_cor -= 10
        self.goto(self.x_cor, self.y_cor)
        self.setheading(270)

    def turn_left(self):
        self.x_cor -= 10
        self.setheading(180)
        self.goto(self.x_cor, self.y_cor)

    def turn_right(self):
        self.x_cor += 10
        self.goto(self.x_cor, self.y_cor)
        self.setheading(0)

    def refresh(self):
        self.x_cor = 0
        self.y_cor = -230
        self.setheading(90)
        self.goto(self.x_cor, self.y_cor)
