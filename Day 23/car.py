from turtle import Turtle
import random

class Car:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.colors = ['blue', 'green', 'red', 'yellow', 'orange', 'purple']
        self.random_x_cor = 0
        self.random_y_cor = 0
        self.car_speed = 2
        self.create_car()

    def create_car(self):
        for _ in range(30):
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(1, 3)
            new_car.setheading(180)
            new_car.penup()
            self.generate_random_cor(new_car)
            new_car.color(random.choice(self.colors))
            self.all_cars.append(new_car)


    def move_car(self, car):
        if car.xcor() < -450:
            self.generate_random_cor(car)
        car.forward(self.car_speed)
        car.screen.update()

    def generate_random_cor(self, car):
        self.random_x_cor = random.randint(400, 1600)
        self.random_y_cor = random.randint(-200, 200)
        car.goto(self.random_x_cor, self.random_y_cor)

    def increase_car_speed(self):
            self.car_speed += 2
