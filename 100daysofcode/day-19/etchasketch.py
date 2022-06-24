from turtle import Turtle, Screen

franklin = Turtle()


def move_forward():
    franklin.forward(10)


def move_backward():
    franklin.backward(10)


def turn_left():
    franklin.left(10)


def turn_right():
    franklin.right(10)


def clear_drawing():
    franklin.clear()
    franklin.penup()
    franklin.home()
    franklin.pendown()


screen = Screen()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_drawing)
screen.exitonclick()
