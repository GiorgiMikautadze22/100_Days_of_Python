import sys
import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title('U.S State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []


data = pandas.read_csv('50_states.csv')

states = data.state.to_list()

score_board = Turtle()
score_board.penup()
score_board.goto(-280, 250)
score_board.hideturtle()
score_board.write(f'{len(guessed_states)}/{len(states)}',align='center', font=("Arial", 18, "normal"))

wrong = Turtle()
wrong.penup()



while len(guessed_states) < len(states):
    tim = Turtle()
    tim.penup()
    answer_state = screen.textinput('Guess the State', prompt="What's another states name?").title()
    wrong.clear()
    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv('states_to_learn.csv')
        sys.exit()


    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        score_board.clear()
        score_board.write(f'{len(guessed_states)}/{len(states)}', align='center', font=("Arial", 18, "normal"))
        row = data[data.state == answer_state]
        tim.shape('circle')
        tim.shapesize(0.2)
        tim.goto(row.x.item(), row.y.item())
        tim.write(row.state.to_list()[0])
    else:
        wrong.hideturtle()
        wrong.goto(0, 250)
        wrong.write('Wrong. Try again',align='center', font= ("Arial", 48, "normal"))


screen.exitonclick()