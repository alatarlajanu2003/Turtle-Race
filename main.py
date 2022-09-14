from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def create_turtle(color_turtle, x, y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_turtle)
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)


x_main = -230
y_main = -100
for i in colors:
    create_turtle(i, x_main, y_main)
    y_main += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
