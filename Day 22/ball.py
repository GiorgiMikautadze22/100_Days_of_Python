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
        self.ball_speed = 0.05
        self.move()


    def move(self):
            time.sleep(self.ball_speed)
            new_x_cor = self.xcor() + self.x_cor
            new_y_cor = self.ycor() + self.y_cor
            self.goto(new_x_cor, new_y_cor)
            self.screen.update()

    def reset(self):
        self.goto(0, 0)

    def increase_ball_speed(self):
        if self.ball_speed <= 0:
            self.ball_speed = 0.001
        else:
            self.ball_speed -= 0.005
