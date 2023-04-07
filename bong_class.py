BAT_POSITION1 = [(-340,0),(-340,20),(-340,-20)]
BAT_POSITION2 = [(330,0),(330,20),(330,-20)]



import turtle



class Bong(turtle.Turtle):
    def __init__(self):
        super().__init__()

    def create(self,position):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.goto(position)
        self.speed(7)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    
