from turtle import Turtle
import random

car_colors = ["cyan", "red", "azure4", "chocolate", "blue", "orange", "gray", "green", "yellow"]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(car_colors))
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len= 1)
        self.setheading(90)
        self.moving_speed = 6
        rand_y = random.randint(-200, 200)
        rand_x = random.randint(-400, 400)
        self.goto(rand_x, rand_y)

    def moving(self):
        new_x = self.xcor() - self.moving_speed
        self.setx(new_x)
        self.reset_car_position()

    def set_car_position(self):
        rand_y = random.randint(-200, 200)
        rand_x = random.randint(400, 1200)
        self.goto(rand_x, rand_y)

    def reset_car_position(self):
        if self.xcor() < -410:
            self.set_car_position()
