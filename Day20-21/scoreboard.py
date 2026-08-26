from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0,270)
        self.refresh_score()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}  High Score: {self.high_score}", False, align="center", font=("Courier", 14, "normal"))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = -1
        self.refresh_score()





