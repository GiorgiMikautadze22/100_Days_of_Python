from turtle import Turtle
import random
import time

class Car(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 3)
        self.setheading(180)
        self.penup()
        self.random_x_cor = 0
        self.random_y_cor = 0
        self.create_car()

    def create_car(self):
        self.generate_random_cor()


    def move_car(self):
        if self.xcor() < -450:
            self.generate_random_cor()
        self.forward(5)
        self.screen.update()

    def generate_random_cor(self):
        self.random_x_cor = random.randint(400, 1600)
        self.random_y_cor = random.randint(-220, 220)
        self.goto(self.random_x_cor, self.random_y_cor)
