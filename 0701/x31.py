n = int(input("输入一个正整数:"))
step = 0
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    step += 1
    print(int(n))
print("从n变化到1的变化次数为:", step)
