from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"L-Score: {self.l_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(200, 250)
        self.write(f"R-Score: {self.r_score}", align="center", font=("Courier", 24, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

