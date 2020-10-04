import turtle


def color(len):
    if len > 24:
        t.pencolor('burlywood4')
    elif len > 12:
        t.pencolor('olive drab')
    elif len > 6:
        t.pencolor('lime green')
    elif len > 3:
        t.pencolor('lawn green')
    else:
        t.pencolor('green yellow')


def tree(branch_len, w):
    if branch_len > 2:
        color(branch_len)
        t.pensize(w)
        t.forward(branch_len)
        t.right(60)
        tree(branch_len * alpha, w * beta)
        t.left(60)
        tree(branch_len * 0.85, w * beta)
        t.left(60)
        tree(branch_len * alpha, w * beta)
        t.right(60)
        color(branch_len)
        t.pensize(w)
        t.backward(branch_len)


alpha = 0.5
beta = 0.85
wid = 10
t = turtle.Turtle()
turtle.tracer(False)
# turtle.delay(0)
t.left(90)
t.penup()
t.backward(150)
t.pendown()
tree(60, wid)

t.hideturtle()
turtle.update()
turtle.done()
