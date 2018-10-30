# 简单选择排序的增强版，间隔改为gap，每次除2

from random import randint
import time


# l = []
#
# for i in range(20):
#     l.append(randint(1, 80))


l = [5, 1, 8, 2, 3, 4, 7, 9, 6]


def fun():
    for m in range(0, len(l)):
        if m + gap < len(l):
            for n in range(m + gap, len(l), gap):
                temp = l[n]
                l[n] = 0
                i = n - gap
                while i >= m:
                    if l[i] > temp:
                        l[i + gap] = l[i]
                        i -= gap
                    else:
                        break
                l[i + gap] = temp
        else:
            break
    print(l)


gap = len(l) // 2
start = time.time()
while gap >= 1:
    fun()
    gap = gap // 2
print(time.time() - start)
