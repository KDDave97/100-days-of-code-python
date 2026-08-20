from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.color("coral")


tim.pensize(5)
tim.speed(0)

directions = [0, 90, 180, 270]

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)

steps = 100

for i in range(steps):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    rand_color()




screen.exitonclick()

