from turtle import Screen
from paddle import Paddles
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddles((350, 0))
left_paddle = Paddles((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")

screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280  or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()