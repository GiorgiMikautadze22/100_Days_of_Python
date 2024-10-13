from turtle import Turtle, Screen
from board import Board
from paddle import Paddle

screen = Screen()
screen.setup(800, 500)
screen.bgcolor('black')
screen.tracer(0)

board = Board()

paddle = Paddle()

screen.listen()
screen.onkey(paddle.down(), 'Down')
screen.onkey(paddle.up(), 'Up')

screen.update()

screen.exitonclick()