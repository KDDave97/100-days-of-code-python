from turtle import Turtle

class Paddles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=10)
        self.goto(x=350, y=0)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)