from turtle import Turtle
FONT = ("Courier", 13, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("black")
        self.display()

    def display(self):
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def add_point(self):
        self.level += 1
        self.clear()
        self.display()

    def finish_indication(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Impact", 26, "normal"))

