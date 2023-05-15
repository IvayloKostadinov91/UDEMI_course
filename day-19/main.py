import turtle
from random import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will winn the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-140, -80, -20, 40, 100, 160]
all_turtles =[]

for turtle_index in range(0, 6):
    new_turtple = Turtle(shape="turtle")
    new_turtple.penup()
    new_turtple.color(colors[turtle_index])
    new_turtple.goto(x=-475, y=y_position[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.ranint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
