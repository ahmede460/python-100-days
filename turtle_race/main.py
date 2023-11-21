from turtle import Turtle, Screen
import random

is_race_on = False

blue_turtle = Turtle()
red_turtle = Turtle()
yellow_turtle = Turtle()
green_turtle = Turtle()
orange_turtle = Turtle()
purple_turtle = Turtle()

screen = Screen()
screen.setup(width=500, height=400)

blue_turtle.shape("turtle")
red_turtle.shape("turtle")
yellow_turtle.shape("turtle")
green_turtle.shape("turtle")
orange_turtle.shape("turtle")
purple_turtle.shape("turtle")

blue_turtle.penup()
red_turtle.penup()
yellow_turtle.penup()
green_turtle.penup()
orange_turtle.penup()
purple_turtle.penup()

blue_turtle.color("blue")
red_turtle.color("red")
yellow_turtle.color("yellow")
green_turtle.color("green")
orange_turtle.color("orange")
purple_turtle.color("purple")

blue_turtle.setpos(x=-240, y=70)
red_turtle.setpos(x=-240, y=40)
yellow_turtle.setpos(x=-240, y=10)
green_turtle.setpos(x=-240, y=-20)
orange_turtle.setpos(x=-240, y=-50)
purple_turtle.setpos(x=-240, y=-80)

userbet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
winner = ""


while is_race_on == False:
    blue_turtle.forward(random.randint(0, 10))
    if blue_turtle.xcor() > 220:
        winner = "blue"
        is_race_on = True

    red_turtle.forward(random.randint(0, 10))
    if red_turtle.xcor() > 220:
        winner = "red"
        is_race_on = True

    yellow_turtle.forward(random.randint(0, 10))
    if yellow_turtle.xcor() > 220:
        winner = "yellow"
        is_race_on = True

    green_turtle.forward(random.randint(0, 10))
    if green_turtle.xcor() > 220:
        winner = "green"
        is_race_on = True

    orange_turtle.forward(random.randint(0, 10))
    if orange_turtle.xcor() > 220:
        winner = "orange"
        is_race_on = True

    purple_turtle.forward(random.randint(0, 10))
    if purple_turtle.xcor() > 220:
        winner = "purple"
        is_race_on = True

if userbet == winner:
    print(f"You win !! the winner is {winner}🏁")
else:
    print(f"You lose 🥲  the winner is {winner}")


screen.exitonclick()