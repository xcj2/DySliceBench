import sys
import copy

def partition(A, p, r):
    x = A[r - 1][1]
    i = p - 1
    for j in range(p, r - 1):
        if A[j][1] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp

    tmp = A[i+1]
    A[i+1] = A[r-1]
    A[r-1] = tmp
    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q + 1, r)
    return A

def babble_sort(A, n):
    for j in range(n):
        for i in range(n-1):
            if A[i+1][1] < A[i][1]:
                tmp = A[i+1]
                A[i+1] = A[i]
                A[i] = tmp
    return A

def stable(A, B):
    for i in range(0, len(A)):
        if A[i][0] != B[i][0]:
            return False
    return True


n = int(sys.stdin.readline())

A = [[x[0], int(x[1])] for x in [y.split() for y in sys.stdin.read().split("\n")[:-1]]]

B = sorted(copy.deepcopy(A), key=lambda x: x[1])
C = quicksort(copy.deepcopy(A), 0, n)

if stable(C, B):
    print('Stable')
else:
    print("Not stable")

for i in C:
    print(*i)