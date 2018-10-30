# 归并排序，递归

o = [6, 3, 2, 9, 7, 2, 1]


def merge(m, n):
    l = []
    a = 0
    b = 0
    i = len(m)
    j = len(n)
    while a < i and b < j:
        if m[a] > n[b]:
            l.append(n[b])
            b += 1
        else:
            l.append(m[a])
            a += 1
    while a < i:
        l.append(m[a])
        a += 1
    while b < j:
        l.append(n[b])
        b += 1
    return l


def sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = sort(l[:mid])
    right = sort(l[mid:])
    return merge(left, right)


print(sort(o))
