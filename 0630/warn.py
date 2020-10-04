import turtle

n = int(input("Please input size:(100~300)"))

t = turtle.Turtle()

# 最底层的黄色
t.color('yellow')
t.pensize(n/10)  # 设置画笔的宽度
t.fillcolor('yellow')
t.begin_fill()
for i in range(3):
    t.forward(n)  # turtle.forward(distance):向当前画笔方向移动distance像素长度
    t.left(120)  # turtle.right(degree):顺时针移动degree°
t.end_fill()

# 黑色边框
t.color('black')
t.left(30)
t.penup()
t.forward(n/25)
t.pendown()
t.right(30)
for i in range(3):
    t.forward(n*37/40)
    t.left(120)

# 叹号
# 1.叹号的圆点
t.penup()
t.goto(0, 0)
t.forward(n/2)
t.left(90)
t.forward(n/5)
t.pendown()
t.circle(0)
# 2.叹号的上半部分
# 2.1 画圆
t.penup()
t.goto(0, 0)
t.right(90)
t.forward(n/2)
t.left(90)
t.forward(n/2)
t.pendown()
t.pensize(n/8 + 1)
t.circle(0)

# 2.2 画下方的三角
t.penup()
t.goto(0, 0)
t.right(90)
t.forward(n/2)
t.left(90)
t.forward(n/3.5)
t.pendown()
t.begin_fill()
t.pensize(1)
t.goto(n*9/16, n/2)
t.goto(n*7/16, n/2)
t.goto(n/2, n/3.5)
t.end_fill()

t.hideturtle()  # 隐藏画笔的turtle形状
turtle.done()  # 启动事件循环,必须是turtle图形程序中的最后一个语句。
