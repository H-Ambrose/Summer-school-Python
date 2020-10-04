class mylist(list):
    def product(self):
        ans = self[0]
        for i in self[1:]:
            ans *= i
        return ans

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError
        ans = mylist()
        for i, j in zip(self, other):
            ans.append(i + j)
        return ans

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError
        mid = [i * j for i, j in zip(self, other)]
        ans = sum(mid)
        return ans


# 给定数据：
s = mylist([1, 2, 3, 4, 5])
a = mylist([6, 7, 8, 9, 0])
# 注释的部分展示了如果输入数据而不是程序里给出数据的代码：
# 如果需要输入可以去掉注释，并定义两个空的mylist类型：s = mylist(), a = mylist()
'''
n = int(input('请输入mylist的长度'))
print('输入mylist的内容：')
for _ in range(n):
    s.append(int(input()))
n = int(input('请输入第二个mylist的长度'))
print('输入mylist的内容：')
for _ in range(n):
    a.append(int(input()))
'''
print('累乘：', s.product())
print('两个mylist对应相加：', s + a)
print('两个mylist对应相乘再相加：', s * a)
