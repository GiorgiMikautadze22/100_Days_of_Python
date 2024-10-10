from turtle import Turtle, Screen


screen = Screen()
tim = Turtle()

def move():
    tim.forward(10)

screen.listen()
screen.onkey(move, 'space')
screen.exitonclick()