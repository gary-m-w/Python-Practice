from turtle import Turtle, Screen
from random import randint

var_dict = {}
turtle_colors = ['red','blue','orange','yellow','green','purple','maroon','indigo','aquamarine','black']
screen = Screen()
screen.setup(width=500, height=400)
turtle_number = int(screen.textinput("How many turtles", "How many turtles are racing today? (max 10)"))
user_bet = screen.textinput(title="Place your bets", prompt="Which turtle will win the race? Enter a color: ")

def starting_line(number):
    global var_dict
    var_dict = {
        'turtle_' + str(i): i
        for i in range(number)
    }
    for i in range(number):
        var_dict[f'turtle_{i}'] = Turtle(shape='turtle')
        var_dict[f'turtle_{i}'].color(turtle_colors[i])
        var_dict[f'turtle_{i}'].penup()
        var_dict[f'turtle_{i}'].goto(x=-230, y=(200-(400/(number+1))*(1+i)))
        var_dict[f'turtle_{i}'].pendown()


def race(number):
    for t in range(number):
        rand_distance = randint(0, 10)
        var_dict[f'turtle_{t}'].forward(rand_distance)
    for t in range(number):
        if var_dict[f'turtle_{t}'].xcor() > 230:
            winning_color = var_dict[f'turtle_{t}'].pencolor()
            if winning_color == user_bet.lower():
                print(f"Congrats! The {winning_color} turtle you bet on was the winner!")
            else:
                print(f"Sorry - the {winning_color} turtle won, but you bet on the {user_bet} turtle.")
            return False
    return True


starting_line(turtle_number)
if user_bet:
    is_race_on = True

while is_race_on:
    is_race_on = race(turtle_number)

screen.exitonclick()