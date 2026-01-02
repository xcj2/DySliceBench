INF = int(1e10)
def merge(A, left, mid, right):
    L = A[left: mid] + [[0, INF]]
    R = A[mid: right] + [[0, INF]]
    i = j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
n = int(input())
f = lambda a: (a[0], int(a[1]))
A = [f(input().split()) for _ in range(n)]
B = A[:]
mergeSort(A, 0, n)
quicksort(B, 0, n - 1)
print("Stable" if A == B else "Not stable")
print(*(f"{a} {b}" for a, b in B), sep="\n")

