import turtle as t
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("maroon")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def dashed_line(turtle, length):
    dash = length / 10
    for _ in range(5):
        turtle.pendown()
        turtle.forward(dash)
        turtle.penup()
        turtle.forward(dash)


def draw_shape(turtle, sides):
    degrees = (sides - 2) * 180
    angle = degrees / sides
    turtle.color(random_color())
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(180 - angle)


def random_walk(turtle, steps):
    turtle.speed(8)
    turtle.width(10)
    headings = [0, 90, 180, 270]
    for _ in range(steps):
        turtle.color(random_color())
        turtle.setheading(random.choice(headings))
        turtle.forward(30)


def draw_circles(turtle, number):
    turtle.speed(0)
    turtle.width(2)
    for _ in range(number*2):
        turtle.circle(150)
        turtle.right(360/number + random.randint(0, 2))
        turtle.color(random_color())


# dashed_line(timmy_the_turtle, 300)
# for i in range(3, 11):
#     draw_shape(timmy_the_turtle, i)
# random_walk(timmy_the_turtle, 100)
draw_circles(timmy_the_turtle, 75)
screen = Screen()
screen.exitonclick()
