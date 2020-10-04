import turtle

size = int(input("Please input size:(20~200)"))

t = turtle.Turtle()
t.color('red')
t.pensize(3)  # 设置画笔的宽度

for i in range(5):
    t.forward(size)  # turtle.forward(distance):向当前画笔方向移动distance像素长度
    t.right(144)  # turtle.right(degree):顺时针移动degree°

t.hideturtle()  # 隐藏画笔的turtle形状
turtle.done()  # 启动事件循环,必须是turtle图形程序中的最后一个语句。
