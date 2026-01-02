#ALDS1_6_C Quick Sort
import sys
# sys.setrecursionlimit(10000)
def partition(A, p, r):
    q = A[r][1]
    j = p
    for i in range(p, r):
        if A[i][1] <= q:
            A[i], A[j] = A[j], A[i]
            j += 1
    A[j], A[r] = A[r], A[j]
    return j


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def merge(A, left, mid, right):
    l = A[left: mid]
    r = A[mid: right]

    l.append([None, float('inf')])
    r.append([None, float('inf')])

    i = 0
    j = 0

    for k in range(left, right, 1):
        if l[i][1] <= r[j][1]:
            A[k] = l[i]
            i += 1
        else:
            A[k] = r[j]
            j += 1


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


n = int(input())
A = []
for i in range(n):
    suit, num = input().split()
    A.append([suit, int(num)])
A1 = A.copy()

quick_sort(A, 0, n-1)
merge_sort(A1, 0, n)

if A != A1:
    print('Not stable')
else:
    print('Stable')

for i in range(n):
    print(' '.join(map(str, A[i])))
