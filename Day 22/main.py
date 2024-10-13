from turtle import Screen
from board import Board
from paddle import Paddle
from ball import Ball
from score import Score


screen = Screen()
screen.setup(800, 500)
screen.bgcolor('black')
screen.tracer(0)

board = Board()
score = Score()

paddle_1 = Paddle(screen, 1)
paddle_2 = Paddle(screen, -1)

screen.listen()
screen.onkeypress(paddle_1.down, 's')
screen.onkeypress(paddle_1.up, 'w')
screen.onkeypress(paddle_2.down, 'Down')
screen.onkeypress(paddle_2.up, 'Up')

game_is_on = True

ball = Ball(screen, paddle_1, paddle_2)

while game_is_on:
    ball.move()
    score.show_score()

    if ball.distance(ball.paddle_2) <= 50 and ball.xcor() >= 330 or ball.distance(ball.paddle_1) <= 50 and ball.xcor() <= -330:
        ball.x_cor *= -1

    if ball.ycor() >= 230 or ball.ycor() <= -230:
        ball.y_cor *= -1

    if ball.xcor() > 400:
        score.score_1 += 1
        ball.reset()
        ball.increase_ball_speed()
        ball.x_cor *= -1
    elif ball.xcor() < -400:
        score.score_2 += 1
        ball.reset()
        ball.increase_ball_speed()
        ball.x_cor *= -1

screen.exitonclick()