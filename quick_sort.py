# 快速排序，用递归
def quick_sort(l):
    left = 0
    right = len(l) - 1
    base = l[left]
    while left < right:
        while right > left:
            if l[right] < base:
                l[left] = l[right]
                break
            right -= 1
        while right > left:
            if l[left] > base:
                l[right] = l[left]
                break
            left += 1
    l[left] = base
    return left  # left左边都是比l[left]小的，右边都是比l[left]大的


def main_quick_sort(l):
    if len(l) > 1:
        left = quick_sort(l)
        return main_quick_sort(l[:left]) + [l[left]] + main_quick_sort(l[left + 1:])
    return l


l = [5, 0, 1, 4, 7, 9, 2, 9, 8]
print(main_quick_sort(l))
# print(quick_sort(l))
# list[:]   左闭右开
