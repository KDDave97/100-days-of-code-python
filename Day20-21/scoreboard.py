from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0,270)
        self.refresh_score()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", False, align="center", font=("Courier", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", False, align="center", font=("Courier", 14, "normal"))



