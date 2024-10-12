from operator import index
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

food = Food()
score = Score()

snake = Snake()
screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score()
        snake.extend()

    #NOTE: Statement loosing when touching the walls
    # if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    #     is_game_on = False
    #     score.game_over()

    #NOTE: Statement of teleporting to the other side of the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        snake.head.goto(snake.head.xcor() * -1, snake.head.ycor())
    elif snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.head.goto(snake.head.xcor(), snake.head.ycor() * -1)

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()