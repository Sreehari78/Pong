from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 35, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)
        self.player_one_score = 0
        self.player_two_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.player_one_score}\t{self.player_two_score}", align=ALIGNMENT, font=FONT)

    def player_one_point(self):
        self.player_one_score += 1

    def player_two_point(self):
        self.player_two_score += 1
