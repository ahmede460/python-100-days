from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(width=1000, height=700)
screen.title("PONG 🎾")
screen.tracer(0)

player = Paddle((-470, 0))
computer = Paddle((470, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, key="w")
screen.onkey(player.move_down, key="s")
screen.onkey(computer.move_up, key="Up")
screen.onkey(computer.move_down, key="Down")

game_speed = 0.1

while 1 == 1:
    time.sleep(game_speed)
    screen.update()

    ball.move()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()

    if player.distance(ball) < 50 and ball.xcor() < -450 or computer.distance(ball) < 50 and ball.xcor() > 450:
        
        ball.bounce_back()
        game_speed *= 0.9

    if ball.xcor() < -500: 

        scoreboard.l_scored()
        ball.setposition(0, 0)
        ball.bounce_back()
        game_speed = 0.1
        

    if ball.xcor() > 500:
        scoreboard.r_scored()
        ball.setposition(0, 0)
        ball.bounce_back()
        game_speed = 0.1

        
    




screen.exitonclick()