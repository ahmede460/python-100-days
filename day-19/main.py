from turtle import Turtle, Screen

friday = Turtle()
myscreen = Screen()


def move_forwards():
    friday.forward(10)

def move_backwards():
    friday.forward(-10)

def turn_left():
    friday.left(10)

def turn_right():
    friday.right(10)



myscreen.listen()
myscreen.onkey(key="w", fun=move_forwards) 
myscreen.onkey(key="s", fun=move_backwards) 
myscreen.onkey(key="a", fun=turn_left) 
myscreen.onkey(key="d", fun=turn_right)
myscreen.onkey(key="c", fun=friday.clear)

myscreen.exitonclick()
