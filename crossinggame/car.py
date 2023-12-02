from turtle import Turtle
import random

RANDCOLOR = ["red", "black", "blue", "green"]
RANDSPEED = [ 1, 5, 10]
RANDXPOS = [250,60,500]

class Car(Turtle):
    
    def __init__(self):
        super().__init__()  

        self.color()
        self.shape("square")   
        self.color(random.choice(RANDCOLOR))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setpos(x=random.choice(RANDXPOS),y=random.randrange(-200, 200))
        self.setheading(180)
        

    def move_forward(self):
        self.forward(random.choice(RANDSPEED))
        if self.xcor() < -250:
            self.setpos(x=250, y=self.ycor())