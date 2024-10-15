from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 3)
        self.setheading(180)
        self.penup()
        self.colors = ['blue', 'green', 'red', 'yellow', 'orange', 'purple']
        self.random_x_cor = 0
        self.random_y_cor = 0
        self.car_speed = 2
        self.create_car()

    def create_car(self):
        self.generate_random_cor()
        self.color(random.choice(self.colors))


    def move_car(self):
        if self.xcor() < -450:
            self.generate_random_cor()
        self.forward(self.car_speed)
        self.screen.update()

    def generate_random_cor(self):
        self.random_x_cor = random.randint(400, 1600)
        self.random_y_cor = random.randint(-200, 200)
        self.goto(self.random_x_cor, self.random_y_cor)

    def increase_car_speed(self):
        self.car_speed += 2
