import turtle
import math

pi = 3.1415926
t = turtle.Turtle()
turtle.setworldcoordinates(-200, -200, 200, 200)

# 画坐标系
t.pencolor("black")
t.pensize(0.5)
t.penup()
t.goto(-200, 0)
t.pendown()
t.goto(200, 0)
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)

# 2cos(2x)
t.penup()
t.goto(-200, 200 / pi)
t.pendown()
t.pencolor("blue")
t.pensize(3)
t.write("y = math.2cos(2x)", font=("consolas", 10, "normal"))
for x in range(-200, 200, 1):
    y = 200 / pi * math.cos(x * pi / 50)
    t.goto(x, y)

# cosx
t.penup()
t.goto(-200, 100 / pi)
t.pendown()
t.pencolor("red")
t.pensize(3)
t.write("y = math.cos(x)", font=("consolas", 10, "normal"))
for x in range(-200, 200, 1):
    y = 100 / pi * math.cos(x * pi / 100)
    t.goto(x, y)

# sin(x)
t.penup()
t.goto(-200, 0)
t.pendown()
t.pencolor("green")
t.pensize(3)
t.write("y = math.sin(x)", font=("consolas", 10, "normal"))
for x in range(-200, 200, 1):
    y = 100 / pi * math.sin(x * pi / 100)
    t.goto(x, y)

t.hideturtle()
turtle.done()
