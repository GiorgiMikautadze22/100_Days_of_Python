# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()
#
# print(timmy)

from prettytable import PrettyTable


table = PrettyTable()
table.add_column('Pokemon', ['Pikachu', 'Gela'])
table.add_column('Type', ['Electric', 'Alcoholic'])
table.align = 'l' #attribute

print(table)