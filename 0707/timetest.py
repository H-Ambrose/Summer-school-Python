import time


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 35):
    start = time.time()
    f = fibonacci(i)
    end = time.time()
    print('第', i, '项:', f, '用时:', end - start, '秒')
