import time

start = time.time()
l = [2, 9, 9, 7, 1, 9, 0, 2, 6, 8]
for m in range(0, len(l) - 1):
    flag = True  # 改进
    for n in range(len(l) - 1, m, -1):
        if l[n - 1] > l[n]:
            temp = l[n]
            l[n] = l[n - 1]
            l[n - 1] = temp
            flag = False
    if flag is True:  # 说明内循环没有被执行，也就是序列已经有序
        break
    print(m, end=' ')
    print(l)

print('total time: ', time.time() - start)
