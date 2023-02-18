import colorgram
import turtle as turt
import random

turt.colormode(255)
timmy = turt.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

dot_size = 20
num_rows = 10
spacing = 50
num_dots = num_rows * num_rows


def get_color_list():
    """ Generate color list from the colors in an image, 'image.jpg' """
    c_list = []
    colors = colorgram.extract("image.jpg", 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        c_list.append(new_color)
    return c_list


def new_row():
    """ Start a new row of dots """
    timmy.setheading(90)
    timmy.forward(spacing)
    # timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(num_rows * spacing)
    # timmy.forward(500)
    timmy.setheading(0)

# color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


color_list = get_color_list()
# Move turtle to starting position
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


for dot_count in range(1, num_dots+1):
    timmy.dot(dot_size, random.choice(color_list))
    timmy.forward(spacing)

    if dot_count % num_rows == 0:
        new_row()

screen = turt.Screen()
screen.exitonclick()
