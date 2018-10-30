# 堆排序，列表索引从0开始，不能用，

l = dict(zip((range(1, 9)), [15, -9, 19, 6, -9, 3, 9, 1]))


def heap_adjust(l, s, e):
    if e == 2:  # 还剩两个元素时，确保第一个是大的
        if l[1] < l[2]:
            l[1], l[2] = l[2], l[1]
    else:
        i = 2 * s
        while i < e:
            if l[i + 1] > l[i]:
                i += 1
            if l[i] > l[s]:
                l[i], l[s] = l[s], l[i]
            s = i
            i = i * 2


for i in range(len(l) // 2, 0, -1):  # 地板除保证了无论列表是单数还是偶数都能运行
    heap_adjust(l, i, len(l))
for i in range(len(l), 1, -1):
    l[1], l[i] = l[i], l[1]
    heap_adjust(l, 1, i - 1)
print(l.values())
