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
from turtle_cross import TurtleCross

screen = Screen()
screen.setup(width=800, height=500)
screen.title('Cross Road Game')
screen.tracer(0)

tim = TurtleCross(screen)

screen.listen()
screen.onkeypress(tim.up, 'Up')
screen.onkeypress(tim.down, 'Down')
screen.onkeypress(tim.turn_left, 'Left')
screen.onkeypress(tim.turn_right, 'Right')




screen.update()



screen.exitonclick()