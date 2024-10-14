from turtle import Turtle


class TurtleCross(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.screen = screen
        self.x_cor = 0
        self.y_cor = 0
        self.refresh()


    def up(self):
        self.y_cor += 10
        self.goto(self.x_cor,self.y_cor)
        self.setheading(90)

        if self.ycor() > 250:
            self.refresh()

        self.screen.update()


    def down(self):
        self.y_cor -= 10
        self.goto(self.x_cor, self.y_cor)
        self.setheading(270)
        self.screen.update()


    def turn_left(self):
        self.x_cor -= 10
        self.setheading(180)
        self.goto(self.x_cor, self.y_cor)
        self.screen.update()


    def turn_right(self):
        self.x_cor += 10
        self.goto(self.x_cor, self.y_cor)
        self.setheading(0)
        self.screen.update()

    def refresh(self):
        self.x_cor = 0
        self.y_cor = -200
        self.setheading(90)
        self.goto(self.x_cor, self.y_cor)
