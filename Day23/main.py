from turtle import Screen
from player import Player
from cars import Cars
from levelhandler import LevelHandler
import time

LEVEL_POSITION = (-340, 270)
GAME_OVER_POSITION = (0, 0)

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
player = Player()
level_handler = LevelHandler(LEVEL_POSITION)
game_over = LevelHandler(GAME_OVER_POSITION)
cars_list = []

screen.listen()
screen.onkeypress(fun=player.move_up, key="w")
screen.onkeypress(fun=player.move_down, key="s")

for i in range(30):
    car = Cars()
    cars_list.append(car)

is_game_on = True
level_handler.increase_level()
while is_game_on:
    screen.update()
    time.sleep(0.05)
    for car in cars_list:
        car.moving()
        if car.distance(player) < 24:
            is_game_on = False
            game_over.game_over()

    if player.ycor() > 250:
        level_handler.increase_level()
        player.goto(0, -280)
        for car in cars_list:
            car.moving_speed += level_handler.level / 2




screen.exitonclick()