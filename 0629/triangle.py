n = int(input("Please input line number: "))
for i in range(n):  # 输出n行
    line = " " * (n - 1 - i) + "@" * (2 * i + 1)
    print(line)
    # 输出n-1-i个空格和2*i+1个@符号
