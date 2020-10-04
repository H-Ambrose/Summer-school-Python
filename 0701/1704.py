import math

n = int(input())
n2 = math.sqrt(n)
flag = 1
for i in range(2, int(n2) + 2, 1):
    if n % i == 0:
        flag = 0
        break
if n == 1:
    flag = 0
if flag == 1 or n == 2:
    print('yes')
else:
    print('no')
