from turtle import Screen
from paddle import Paddles

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=800)
screen.title("Pong")

right_paddle = Paddles()

screen.listen()
screen.onkeypress(fun=right_paddle.move_up, key="w")
screen.onkeypress(fun=right_paddle.move_down, key="s")


screen.exitonclick()