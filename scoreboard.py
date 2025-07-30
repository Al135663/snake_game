from turtle import Turtle
FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial",20,"normal"))
        self.hideturtle()


    def game_over(self):
        self.goto(0, 100)
        self.color("red")
        self.write("!!  GAME OVER  !!", align="center", font=("Arial",30,"italic"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)