import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
color_list = [(241, 223, 83), (32, 98, 189), (174, 65, 34), (82, 175, 220), (191, 15, 32), (219, 158, 81), (78, 108, 211), (176, 47, 87), (226, 57, 103), (161, 164, 20), (166, 28, 17), (73, 177, 77), (234, 69, 42), (229, 120, 172), (125, 200, 112), (20, 54, 146), (58, 118, 62), (116, 226, 185), (70, 31, 44), (134, 217, 234), (239, 157, 217), (162, 163, 235), (38, 175, 184), (243, 174, 151), (31, 40, 84), (93, 29, 21)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()