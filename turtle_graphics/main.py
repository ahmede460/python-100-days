import turtle as t
import random

#Objects Creation
friday = t.Turtle()
main_screen = t.Screen()


#Setting the turtle attributes
friday.shape("circle")
t.colormode(255)
#friday.color("black")

colors = [(240, 238, 235), (225, 229, 234), (235, 230, 234), (234, 238, 236), (136, 169, 200), (191, 162, 140), (64, 89, 135), (183, 153, 171), (119, 77, 99), (153, 75, 50)]

possiblepaths = [0, 180, 270, 90]
friday.pensize(1)
height = -300

friday.penup()
friday.setpos(-330, height)

for y in range (13):
    for x in range (14):
        friday.color(random.choice(colors))
        friday.dot(20)
        friday.penup()
        friday.forward(50)

    height += 50
    friday.setpos(-330,(height))
    


    


#Screen methods
main_screen.exitonclick()