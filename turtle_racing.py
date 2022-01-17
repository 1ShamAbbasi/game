from turtle import Turtle , Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500 , height=400)
user_input = screen.textinput(title="Make your bet", prompt= "Which turtle win the race ? Enter a color:  ")
colors = ['red', 'green', 'yellow', 'purple', 'black', 'pink']
y_direction = [-70 , -40 , -10 , 20 , 50 , 80]
all_turtol = []


for tutle_index in range(0 , 6):
    timy = Turtle(shape="turtle")
    timy.penup()
    timy.color(colors[tutle_index])
    timy.goto(x=-230 , y= y_direction[tutle_index])
    all_turtol.append(timy)

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtol:
        if turtle.xcor() > 230 :
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_input:
                print(f"You've won {wining_color} turtle is  the winner")
            else :
                print(f"You've loss {wining_color} turtle is  the winner")



        distance=random.randint(0, 10)
        turtle.forward(distance)





screen.exitonclick()