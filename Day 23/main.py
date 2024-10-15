#TODO: create screen and disable tracer
#TODO: Create turtle class that can move on key binds
#TODO: After turtle crosses the road direct it back to starting point
#TODO: Create Car class
#TODO: Cars should randomly be generated outside of the screen ( certain amount )
#TODO: Cars should be different colors
#TODO: Cars should move from right to left at a certain speed
#TODO: When cars reach the end of the road they should be randomly regenerated from the start of the screen
#TODO: When car hits the turtle game over
#TODO: After turtle crosses the road increase level and speed

from turtle import Screen, Turtle
from turtle_cross import TurtleCross
from car import Car
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=500)
screen.title('Cross Road Game')
screen.tracer(0)

score = ScoreBoard()

cars = []
game_is_over = True


tim = TurtleCross(screen)
game_over_title = Turtle()
game_over_title.hideturtle()



screen.listen()
screen.onkeypress(tim.up, 'Up')
screen.onkeypress(tim.down, 'Down')
screen.onkeypress(tim.turn_left, 'Left')
screen.onkeypress(tim.turn_right, 'Right')

for num in range(30):
    car = Car()
    cars.append(car)
screen.update()

def increase_speed():
    for item in cars:
        item.increase_car_speed()


while game_is_over:

    if tim.ycor() >= 240:
        score.increase_score()
        tim.refresh()
        screen.update()
        increase_speed()

    for car in cars:
        car.move_car()
        if car.distance(tim.xcor() + 20, tim.ycor() + 5) < 20 or car.distance(tim.xcor() - 20, tim.ycor() - 5) < 20:
            game_is_over = False
            screen.onkeypress(None, 'Up')
            screen.onkeypress(None, 'Down')
            screen.onkeypress(None, 'Left')
            screen.onkeypress(None, 'Right')
            game_over_title.write('Game Over', align='center', font=("Arial", 45, "normal"))

    screen.update()

screen.exitonclick()