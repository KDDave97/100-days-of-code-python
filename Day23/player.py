from turtle import Turtle

MOVE_SPEED = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move_up(self):
        new_y = self.ycor() + MOVE_SPEED
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_SPEED
        self.sety(new_y)
