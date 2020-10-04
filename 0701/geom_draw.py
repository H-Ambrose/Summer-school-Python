import turtle
import random


def polygon(n, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(n):
        t.forward(size)
        t.left(360 / n)
    t.end_fill()


t = turtle.Turtle()
turtle.delay(0)
turtle.screensize(800, 800)
colors = ['midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green']

# ["red", "green", "yellow", "blue", "brown", "pink", "purple", "orange"]
t.pensize(3)
for _ in range(70):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    nn = random.randint(3, 10)
    sizeie = random.randint(5, 50)
    c = random.choice(colors)
    t.pencolor(c)
    t.penup()
    t.goto(x, y)
    t.pendown()
    polygon(nn, sizeie, c)

t.hideturtle()
turtle.done()
