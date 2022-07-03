import time
from turtle import Screen, Turtle
from snakebrain import Snake
from Food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

game_is_on = True
while game_is_on:
    if snake.boundary_hit():
        game_is_on = False
    screen.update()
    time.sleep(0.05)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    #collision with tail
    if snake.tail_hit():
        game_is_on = False

scoreboard.game_over()
screen.exitonclick()
