# coding: utf-8
import copy

def partition(A, p, r):
    r -= 1
    i = p - 1
    x = A[r][1]
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
    
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q+1, r)

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    L = A[left:mid] + [('dummy', float('inf'))]
    R = A[mid:right] + [('dummy', float('inf'))]
    i = 0
    j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

if __name__ == "__main__":
    # n = 6
    # A = [('D', 3), ('H', 2), ('D', 1), ('S', 3), ('D', 2), ('C', 1)]
    n = int(input())
    A = []
    for _ in range(n):
        mark, num = input().split()
        num = int(num)
        A.append((mark, num))
    B = copy.deepcopy(A)

    quick_sort(A, 0, len(A))
    merge_sort(B, 0, len(B))

    if A == B:
        print('Stable')
    else:
        print('Not stable')

    for i in A:
        print('{} {}'.format(i[0], i[1]))
