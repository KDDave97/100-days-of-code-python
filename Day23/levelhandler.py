from turtle import Turtle

class LevelHandler(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.level = 0
        self.clear()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 16, "normal"))

    def game_over(self):
        self.write(f"Game Over", align="center", font=("Courier", 20, "bold"))

