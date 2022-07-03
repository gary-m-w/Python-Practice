from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-MOVE_DISTANCE, 0), (-2 * MOVE_DISTANCE, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            self.snake[segment].goto(self.snake[segment - 1].position())
        self.snake[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def grow(self):
        self.add_segment(self.snake[-1].position())

    def boundary_hit(self):
        if self.snake[0].xcor() >= 280 or self.snake[0].xcor() <= -280 or self.snake[0].ycor() >= 280 or self.snake[0].ycor() <= -280:
            return True

    def tail_hit(self):
        for segment in self.snake[1:]:
            if self.snake[0].distance(segment) < 10:
                return True

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)