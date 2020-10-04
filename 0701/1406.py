def count_str(s):
    return s.count('1', 0)


n = int(input())
cnt = 0
for i in range(1, n + 1, 1):
    cnt += count_str(str(i))
print(cnt)
