import turtle
import math
import random

turtle.tracer(False)
t = turtle.Turtle()
turtle.setworldcoordinates(0, 0, 1, 1)

# 画坐标系
t.pencolor("black")
t.pensize(1)
t.penup()
t.goto(1, 0)
t.pendown()

for x in range(200, 0, -1):
    x /= 200
    y = math.sqrt(1 - x * x)
    t.goto(x, y)

cnt = 0
for _ in range(10000):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    b = x * x + y * y
    t.penup()
    t.goto(x, y)
    t.pendown()
    if b <= 1:
        t.dot(5, 'red')
        cnt += 1
    else:
        t.dot(5, 'blue')

pi = 4 * cnt / 10000
print("估算出的π值", pi)

t.hideturtle()
turtle.done()
turtle.update()
