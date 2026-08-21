from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.color("coral")

tim.pensize(1)
tim.speed(0)

directions = [0, 90, 180, 270]

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def spirograph():
    angle = 0
    while angle < 360:
        tim.circle(100)
        tim.setheading(angle)
        angle += 7
        tim.color(rand_color())

def star():
    tim.begin_fill()
    tim.color(rand_color())
    while True:
        tim.forward(200)
        tim.left(170)
        if abs(tim.pos()) < 1:
            break
    tim.end_fill()

def path():
    tim.pensize(15)
    steps = 100
    for i in range(steps):
        tim.color(rand_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))
        rand_color()

def hirst():
    dots = 0
    row_count = 0
    tim.teleport(-350, -350)
    tim.penup()
    tim.ht()
    while dots < 100:
        while row_count < 10:
            tim.dot(20, rand_color())
            tim.setx(tim.xcor() + 50)
            dots += 1
            row_count += 1
        row_count = 0
        tim.teleport(-350, tim.ycor() + 50)

hirst()
screen.exitonclick()

