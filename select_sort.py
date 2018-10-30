# l = [9, 5, 7, 3, 2, 29, 62, 1, 3, 78, ]

from random import randint
import time

l = []

for i in range(20):
    l.append(randint(1, 80))

for m in range(0, len(l) - 1):  # 从索引0开始，到倒数第二个
    temp = m
    for n in range(m + 1, len(l)):  # 找出未排序序列中比l[m]小的那个索引
        if l[n] < l[temp]:
            temp = n

    if temp != m:
        a = l[m]
        l[m] = l[temp]
        l[temp] = a
    print(l)
