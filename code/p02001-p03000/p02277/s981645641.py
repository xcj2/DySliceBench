import copy
import sys

def partition(A, p, r):
    key = A[r][1]
    i = p
    for j in range(p, r):
        # 把小的放在左边
        if A[j][1] <= key:
            A[i], A[j] = A[j], A[i]
            i += 1
    # 最后交换key值
    A[r], A[i] = A[i], A[r]
    return i

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def merge(A, left, mid, right):
    L = A[left: mid] + [(0, sys.maxsize)]
    R = A[mid: right] + [(0, sys.maxsize)]
    i = j = 0
    k = left
    while k < right:
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

def merge_sort(A, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


if __name__ == '__main__':
    n = int(input())
    numlist = []
    for _ in range(n):
        datas = input().split(' ')
        numlist.append((datas[0], int(datas[1])))
    list2 = copy.deepcopy(numlist)
    quick_sort(numlist, 0, n - 1)
    merge_sort(list2, 0, n)
    if list2 == numlist:
        print('Stable')
    else:
        print('Not stable')
    for c, num in numlist:
        print('%s %d' % (c, num))
