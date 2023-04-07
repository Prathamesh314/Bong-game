import turtle
import bong_class
from score_board import ScoreBoard
from ball import Ball
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("The Bong Game")
n = screen.textinput(title="Traget",prompt="How many points match you want to paly: ")
score = ScoreBoard()
right_paddle = bong_class.Bong()
left_paddle = bong_class.Bong()
right_paddle.create((360,0))
left_paddle.create((-370,0))
ball = Ball()
ball.speed(1)
screen.tracer(0)

screen.setup(width=800,height=600)

new_line = turtle.Turtle("square")
new_line.color("white")
new_line.penup()
new_line.width(7)
new_line.goto(0,300)
new_line.setheading(270)
for i in range(580):
    new_line.speed("fastest")
    new_line.forward(30)
    new_line.penup()
    new_line.forward(30)
    new_line.pendown()


game_is_on = True
screen.listen()
screen.onkeypress(fun=right_paddle.up,key="Up")
screen.onkeypress(fun=right_paddle.down,key="Down")
screen.onkeypress(fun=left_paddle.up,key="w")
screen.onkeypress(fun=left_paddle.down,key="s")

while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.right_up()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.refresh()
        score.l_score_increase()
    if ball.xcor() < -390:
        ball.refresh()
        score.r_score_increase()
       


screen.exitonclick()