from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.color("coral")

# for i in range(15):
#     tim.forward(10)
#     tim.teleport(tim.xcor() + 10, tim.ycor())


tim.teleport(-50, tim.ycor() + 350)
sides = 3
while sides < 20:
    angle = 360 / sides
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)
    sides += 1
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)



# turn = 4
# angle = 360 / turn
# for i in range(turn):
#     tim.forward(100)
#     tim.right(angle)
screen.exitonclick()

