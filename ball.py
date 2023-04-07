
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.xmove = 10
        self.ymove = 10
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed(3)
        self.move_speed = 0.1

    def right_up(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.ymove *= -1
        self.move_speed *= 0.9
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    def refresh(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1


    


