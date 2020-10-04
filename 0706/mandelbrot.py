import turtle
import math
import random

t = turtle.Turtle()
turtle.tracer(False)
# t.speed(0)
turtle.setworldcoordinates(-2, -1.5, 1, 1.5)


def calculate(c):
    z = c
    for i in range(100):
        if abs(z) > 2:
            return False
        z = z**2 + c
    return True


for x in range(-400, 200, 2):
    for y in range(-300, 300, 2):
        c = complex(x / 200, y / 200)
        if calculate(c):
            t.penup()
            t.goto(c.real, c.imag)
            t.pendown()
            t.dot(3.5, 'black')


t.hideturtle()
turtle.update()
turtle.done()
