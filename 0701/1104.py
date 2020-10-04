n = int(input())
sumie = 0
for i in range(1, n + 1, 1):
    s = str(i)
    if i % 7 == 0 or s.find('7') != -1:
        continue
    sumie += i
print(sumie)
