import turtle
import random

colors = ['magenta2', 'magenta3', 'orchid1', 'orchid2', 'orchid3', 'plum1',
          'plum2', 'MediumOrchid1', 'MediumOrchid2', 'DarkOrchid1',
          'DarkOrchid2', 'DarkOrchid3', 'purple1', 'purple2', 'purple3',
          'MediumPurple1', 'MediumPurple2', 'MediumPurple3']


def color(len):
    if len > 24:
        t.pencolor('brown4')
    # elif len > 6:
    #    t.pencolor('saddle brown')
    else:
        t.pencolor('VioletRed4')


def tree(branch_len, trunks, times):  # branch_len:枝干长度，w:枝干长度的偏移量，trunks:枝干宽度
    if times > 0:  # branch_len > 10
        longth = random.randint(int(branch_len - wid), int(branch_len + wid))
        color(abs(longth))
        t.pensize(trunks)
        x, y = t.pos()
        t.forward(abs(longth))
        n = random.randint(2, 3)
        delta = random.randint(-5, 5)
        if n == 3:
            t.right(20 + delta)
            tree(branch_len * alpha, trunks * gamma, times - 1)
            t.left(20)
            tree(branch_len * alpha, trunks * gamma, times - 1)
            t.left(20)
            tree(branch_len * alpha, trunks * gamma, times - 1)
            t.right(20 - delta)
            color(longth)
            t.penup()
            t.goto(x, y)
            t.pendown()
            # t.backward(abs(longth))
        else:
            t.right(20 + delta)
            tree(branch_len * alpha, trunks * gamma, times - 1)
            t.left(40 + delta)
            tree(branch_len * alpha, trunks * gamma, times - 1)
            t.right(20)
            color(longth)
            t.penup()
            t.goto(x, y)
            t.pendown()
            # t.backward(abs(longth))

    else:
        degree = random.randint(-10, 10)
        if degree < 0:
            t.right(abs(degree))
        else:
            t.left(degree)
        t.pencolor(random.choice(colors))
        t.pensize(4)
        t.forward(5)
        if degree < 0:
            t.left(abs(degree))
        else:
            t.right(degree)
        t.backward(5)


def subbackground(x1, x2, y1, y2):
    for _ in range(100):
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        t.penup()
        t.goto(x, y)
        t.pendown()
        degree = random.randint(-10, 10)
        if degree < 0:
            t.right(abs(degree))
        else:
            t.left(degree)
        t.pencolor(random.choice(colors))
        t.pensize(3)
        t.forward(4)
        if degree < 0:
            t.left(abs(degree))
        else:
            t.right(degree)


def backgraoud():
    for _ in range(300):
        x = random.randint(-400, 400)
        y = random.randint(-150, 350)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(2, 'snow')
    subbackground(-400, 400, -300, -140)
    subbackground(-200, 200, -200, -140)
    subbackground(-150, 150, -170, -140)
    subbackground(-100, 100, -150, -140)
    t.penup()
    t.goto(0, 0)
    t.pendown()


alpha = 0.9
beta = 0.9
gamma = 0.8
wid = 5
trunk = 8
# times = 10
t = turtle.Turtle()
# turtle.tracer(False)
turtle.delay(0)
# turtle.bgcolor('midnight blue')
turtle.bgcolor('black')
# 原background
backgraoud()

t.left(80)
t.penup()
t.backward(150)
t.pendown()
t.pencolor('brown4')
t.pensize(10)
t.right(5)
t.forward(22)
t.pensize(trunk)
t.left(10)
t.forward(17)
t.left(5)
tree(45, trunk, 10)
##
subbackground(-150, 150, -170, -140)
##

t.hideturtle()
# turtle.update()
turtle.done()
