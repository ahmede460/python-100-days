from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=0,y= 270)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score} 🐍", align="center", font=("Arial", 18, "normal"))



    def game_over(self):
        self.setpos(x=0, y=0)
        self.write(f"Game Over 😭", align="center", font=("Arial", 18, "normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()