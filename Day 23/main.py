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

from turtle import Screen
from player import Player
from car import Car
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=500)
screen.title('Cross Road Game')
screen.tracer(0)

cars = Car()
score = ScoreBoard()
player = Player()

game_is_over = True

screen.listen()
screen.onkeypress(player.up, 'Up')
screen.onkeypress(player.down, 'Down')
screen.onkeypress(player.turn_left, 'Left')
screen.onkeypress(player.turn_right, 'Right')

while game_is_over:
    # Checks what to do after player crosses the finish line
    if player.ycor() >= 240:
        score.increase_score()
        player.refresh()
        cars.increase_car_speed()

    for car in cars.all_cars:
        cars.move_car(car) # Moves a car forward
        # Colliding check
        if car.distance(player.xcor() + 20, player.ycor() + 5) < 20 or car.distance(player.xcor() - 20, player.ycor() - 5) < 20:
            game_is_over = False
            screen.onkeypress(None, 'Up')
            screen.onkeypress(None, 'Down')
            screen.onkeypress(None, 'Left')
            screen.onkeypress(None, 'Right')
            score.game_over()

    screen.update()

screen.exitonclick()