# import random
#
# l = []
# for i in range(30):
#     l.append(random.randint(1, 100))
l = [9, 1, 8, 2, 3, 4, 7, 9, 6]
# l_temp = l[0:1]
# print(ll)


#############
# for m in range(1, len(l)):
#     # print(m, end=' ')
#     for n in range(m - 1, -1, -1):
#         if l[m] < l[0]:
#             temp = l.pop(m)
#             l.insert(0, temp)
#             break
#         # print(n, end=' ')
#         if l[m] >= l[n]:
#             temp = l.pop(m)
#             l.insert(n + 1, temp)
#             break 
# print(l)
for m in range(1, len(l)):
    print('m:', m, end=' ')
    temp = l[m]
    l[m] = 0
    print('temp:', temp, end='  ')
    n = m - 1
    while n >= 0:
        if l[n] > temp:  # 如果大于就依次向前移
            l[n + 1] = l[n]
            n -= 1
        else:
            break
    l[n + 1] = temp
    print(l)
