from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
timmy =Turtle()

# num_of_sides = 3
#
# while num_of_sides != 10:
#     degree = 360 // num_of_sides
#     for _ in range(num_of_sides):
#         timmy.forward(50)
#         timmy.right(degree)
#     num_of_sides += 1


# timmy.pensize(15)
# timmy.shape('circle')
# timmy.speed('fastest')
# direction = [0, 90, 180, 270]
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(direction))
#     timmy.forward(25)

timmy.speed('fastest')
angle = 5
repeat = 360 // angle

for _ in range(repeat):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(angle)
    angle += 5

screen = Screen()
screen.exitonclick()