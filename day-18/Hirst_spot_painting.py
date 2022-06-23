import turtle
import random

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# color_list copied from the above output, minus the shades of white
color_list = [(53, 107, 131), (177, 78, 34), (199, 142, 34), (116, 156, 171), (123, 80, 98), (124, 175, 157),
              (226, 197, 130), (190, 88, 110), (55, 38, 19), (12, 49, 63), (43, 168, 128), (51, 126, 121),
              (197, 124, 143), (166, 21, 31), (222, 93, 79), (243, 163, 160), (38, 32, 35), (4, 25, 24), (80, 147, 168),
              (161, 26, 23), (19, 79, 92), (233, 167, 172), (175, 207, 187), (101, 127, 158), (165, 203, 210)]


painter = turtle.Turtle()
painter.speed("fastest")
turtle.colormode(255)


def paint_dots(rows, columns, dotsize, spacesize):
    painter.hideturtle()
    painter.penup()
    painter.setposition(-spacesize * columns / 2, -spacesize * rows / 2)
    for _ in range(rows):
        painter.setheading(0)
        for _ in range(columns):
            painter.color(random.choice(color_list))
            painter.pendown()
            painter.dot(size=dotsize)
            painter.penup()
            painter.forward(spacesize)
        painter.back(spacesize * columns)
        painter.setheading(90)
        painter.forward(spacesize)


paint_dots(10, 10, 25, 40)
screen = turtle.Screen()
screen.exitonclick()
