def swap(a, i, j):
    # list aのi番目の要素とj番目の要素を交換する関数
    k = a[j]
    a[j] = a[i]
    a[i] = k


def selectionSort(a, n):
    for i in range(n):
        minj = i
        for j in range(i,n):
            if a[j][1] < a[minj][1]: #数字が１桁なのでstrのまま比較可能
                minj = j
        swap(a, i, minj)


def bubbleSort(a, n):
    flag = 1
    while flag:
        flag = 0
        for j in range(n-1,0,-1):
            if a[j][1] < a[j-1][1]:
                swap(a, j-1, j)
                flag = 1


n = int(input())
a = list(input().split())
b = a[:]
bubbleSort(a, n)
print(' '.join(a))
print('Stable')
selectionSort(b, n)
print(' '.join(b))
if a == b:
    print('Stable')
else:
    print('Not stable')

