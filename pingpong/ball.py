from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.x_move + self.xcor()
        new_y = self.y_move + self.ycor()
        self.setposition(new_x, new_y)
    
    def bounce(self):

        self.y_move *=-1

    def bounce_back(self):

        self.x_move *=-1