from turtle import Turtle
ALINGMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.scorecard()
        self.hideturtle()

    def update_score(self):
        self.score += 1 #-my method for scorecard
        # wrote this later because score was flashing slowly
        self.clear()
        self.scorecard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALINGMENT, font=FONT)

    def scorecard(self):
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)
