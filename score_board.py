from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    
    def update(self):
        self.clear()
        self.goto(0,240)
        self.write("SCORE",align='center',move=False,font=("Bahnschrift Condensed",40,"normal"))
        self.goto(-100,200)
        self.write(self.l_score,align='center',move=False,font=("Bahnschrift Condensed",40,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align='center',move=False,font=("Bahnschrift Condensed",40,"normal"))

    def l_score_increase(self):
        self.l_score+=1
        self.update()
    def r_score_increase(self):
        self.r_score += 1
        self.update()