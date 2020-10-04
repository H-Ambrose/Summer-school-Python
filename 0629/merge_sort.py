# 归并排序
import random


def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list  # 不需排序直接返回
    middle = int(len(data_list) / 2)
    left = merge_sort(data_list[:middle])  # 排列左半部分
    right = merge_sort(data_list[middle:])  # 排列右半部分
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)  # 将合并后left或者right中剩下的部分直接加入merged
    return merged


data_list = [random.randint(1, 100) for _ in range(50)]
# print(data_list) 打印生成的随机数组
print(merge_sort(data_list))