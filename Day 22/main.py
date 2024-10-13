import sys
from turtle import Turtle, Screen
from board import Board
from paddle import Paddle
from ball import Ball
import time
from score import Score


screen = Screen()
screen.setup(800, 500)
screen.bgcolor('black')
screen.tracer(0)
time.sleep(0.025)

board = Board()
score = Score()

paddle_1 = Paddle(screen, 1)
paddle_2 = Paddle(screen, -1)

screen.listen()
screen.onkeypress(paddle_1.down, 'Down')
screen.onkeypress(paddle_1.up, 'Up')
screen.onkeypress(paddle_2.down, 's')
screen.onkeypress(paddle_2.up, 'w')

screen.update()
game_is_on = True

ball = Ball(screen, paddle_1, paddle_2)

while game_is_on:
    ball.move()
    if ball.xcor() > 400:
        score.score_1 += 1
        score.show_score()
        game_is_on = False
    elif ball.xcor() < -400:
        score.score_2 += 1
        score.show_score()
        game_is_on = False

    if not game_is_on:
        user_choice = screen.textinput(prompt='Do you want to play again? y or n', title='')
        if user_choice == 'y':
            game_is_on = True
            ball.reset()
            score.hide_score()
        else:
            sys.exit()

screen.exitonclick()