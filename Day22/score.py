from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(position)
        self.points = 0
        self.write(self.points, align="center", font=("Courier", 60, "normal"))

    def score_points(self):
        self.points += 1
        self.clear()
        self.write(self.points, align="center", font=("Courier", 60, "normal"))


