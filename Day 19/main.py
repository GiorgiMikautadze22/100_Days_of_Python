import random
from turtle import Turtle, Screen
from winreg import FlushKey

screen = Screen()
screen.setup(500, 400)
user_guess = screen.textinput('Make your bet','Which turtle will win. Choose color: ')
print(user_guess)

colors = ['blue', 'green', 'yellow', 'red']
turtles = []

pos_count = -100



for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, pos_count)
    pos_count += 50
    turtles.append(new_turtle)

is_race_on = False

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_guess:
                print(f'You won. The winner is {winner} turtle!')
            else:
                print(f'You lost. The winner is {winner} turtle')
        speed = random.randint(0, 10)
        turtle.forward(speed)



screen.listen()
screen.exitonclick()