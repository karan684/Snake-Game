from turtle import Turtle
ALINGMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.scorecard()
        self.hideturtle()

    def update_score(self):
        self.score += 1 #-my method for scorecard
        # wrote this later because score was flashing slowly
        self.scorecard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.scorecard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALINGMENT, font=FONT)

    def scorecard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALINGMENT, font=FONT)
