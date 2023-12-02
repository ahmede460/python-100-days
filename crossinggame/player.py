from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setposition(x= 0, y= -230)
        self.left(90)


    def move(self):
        self.forward(20)