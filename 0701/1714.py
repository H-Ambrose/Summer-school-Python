import math


def isprime(n):
    n2 = math.sqrt(n)
    flag = 1
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n2) + 2, 1):
        if n % i == 0:
            return False
    return True


a = int(input())
b = int(input())
cnt = 0
for i in range(a, b + 1, 1):
    if isprime(i):
        cnt += 1
print(cnt)
