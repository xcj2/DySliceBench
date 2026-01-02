n = int(input())

A = []
B = []

for i in range(n):
    arr = input().split()
    A.append(arr)
    B.append(arr)

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [['x', 0]] * (n1 + 1)
    R = [['x', 0]] * (n2 + 1)

    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1][1] = 1.0e+9 + 1
    R[n2][1] = 1.0e+9 + 1
    i = 0
    j = 0
    for k in range(left, right):
        if int(L[i][1]) <= int(R[j][1]):
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


def partition(A, p, r):
    x = int(A[r][1])
    i = p - 1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


quicksort(A, 0, n-1)
mergeSort(B, 0, n)

stable = True
for i in range(n):
    if A[i] != B[i]:
        stable = False

if stable:
    print('Stable')
else:
    print('Not stable')

for i in range(n):
    print("{} {}".format(A[i][0], A[i][1]))


