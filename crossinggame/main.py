from turtle import Screen
from player import Player
from car import Car
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=500, height=500)
turtle1 = Player()

cars = []

for _ in range(10):
    car = Car()
    cars.append(car)



screen.listen()
screen.onkey(turtle1.move, key="Up")


game_is_on = True

while game_is_on == True:

    time.sleep(0.1)
    screen.update()

    for everycar in cars:
     everycar.move_forward()

    for everycar in cars:
       if everycar.distance(turtle1) < 20:
          game_is_on = False














screen.exitonclick()