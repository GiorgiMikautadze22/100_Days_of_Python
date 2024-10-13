from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self,screen, paddle_1, paddle_2):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('green')
        self.screen = screen
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2
        self.x_cor = 10
        self.y_cor = 10
        self.move()


    def move(self):

            if self.distance(self.paddle_2) <= 50 and self.xcor() >= 330 or self.distance(self.paddle_1) <= 50 and self.xcor() <= -330:
                self.x_cor *= -1

            if self.ycor() >= 230 or self.ycor() <= -230:
                self.y_cor *= -1



            time.sleep(0.05)
            new_x_cor = self.xcor() + self.x_cor
            new_y_cor = self.ycor() + self.y_cor
            self.goto(new_x_cor, new_y_cor)
            self.screen.update()

    def reset(self):
        self.home()
