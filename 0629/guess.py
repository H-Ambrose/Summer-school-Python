# 猜数字游戏
import random

secret = random.randint(1, 100)
print('''猜数游戏！
我想了一个1-100的整数，你最多可以猜六次，
看看能猜出来吗？''')
tries = 1
while tries <= 6:
    guess = int(input("1-100的整数，第%d次猜，请输入： " % (tries,)))
    if guess == secret:
        print("恭喜答对了！你只猜了%d次！\n就是这个： %d! " % (tries, secret))
        break
    elif guess > secret:
        print("不好意思，你的数大了一点儿！ ")
    else:
        print("不好意思，你的数小了一点儿！ ")
    tries += 1
else:
    print("哎呀！怎么也没猜中！再见！ ")
# Python 里面 else 可以和 while 循环或者 for 循环搭配使用
# 用法：
# 当 while/for 循环正常执行完的情况下，执行 else 输出；
# 如果当 while/for 循环中执行了跳出循环的语句，比如 break，将不执行 else 代码块的内容；
