from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0  #An attribute
        self.r_score = 0  #An attribute
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1  #updating l_score
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1  #updating r_score
        self.update_scoreboard()
