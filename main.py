import random
import turtle as turtle_module

turtle_module.colormode(255)
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

mnk = turtle_module.Turtle()
screen = turtle_module.Screen()

screen.setup(800, 800)
screen.title("Hirst Painting")
mnk.speed("fastest")
mnk.setheading(225)
mnk.penup()
mnk.hideturtle()
mnk.forward(300)
mnk.setheading(0)

num_dots = 100
for dot_count in range(1, num_dots + 1):
    mnk.dot(20, random.choice(color_list))
    mnk.forward(50)

    if dot_count % 10 == 0:
        mnk.setheading(90)
        mnk.forward(50)
        mnk.setheading(180)
        mnk.forward(500)
        mnk.setheading(0)

screen.exitonclick()