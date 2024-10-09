# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# tuple_list = []
#
# for color in colors:
#     tuple_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(tuple_list)
import random
import turtle
from turtle import Turtle, Screen, pos

colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

turtle.colormode(255)
timmy = Turtle()
timmy.penup()
timmy.hideturtle()


def draw():
    # timmy.fillcolor(random_color())
    # timmy.begin_fill()
    # timmy.circle(20)
    # timmy.end_fill()
    timmy.dot(20, random.choice(colors))



def teleport():
    timmy.speed('fastest')

    timmy.setpos(x, y)

x = -350
y = -350

for num in range(1, 101):
    teleport()
    draw()
    if num % 10 == 0:
        y += 50
        x = -350
    else:
        x += 50


screen = Screen()
screen.exitonclick()