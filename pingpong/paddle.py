from turtle import Turtle

Y_INITIAL_POSITIONS = [0, -20, -40, -60, -80]
Y_ENEMY_INITIAL_POSITIONS = [350, 330, 310, 290, 270]
class Paddle(Turtle):

    def __init__(self, position_tupple):
        super().__init__()
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position_tupple)
        
    def move_up(self):
        y_current_pos = self.ycor()
        self.sety(y_current_pos + 20)
        

    def move_down(self):
        y_current_pos = self.ycor()
        self.sety(y_current_pos - 20)
        