n = int(input())
A = [input().split(" ") for _ in range(n)]
S = A.copy()

def partition(A, p, r):
    x = int(A[r][1])
    i = p -1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

SENTINEL = 9999999999999

def merge(S, n, left, mid, right):
    global SENTINEL
    n1 = mid - left
    n2 = right - mid
    L = S[left:mid] + [[" ", SENTINEL]]
    R = S[mid:right] + [[" ", SENTINEL]]
    i = j = 0
    for k in range(left, right):
        if int(L[i][1]) <= int(R[j][1]):
            S[k] = L[i]
            i += 1
        else:
            S[k] = R[j]
            j += 1

def mergeSort(S, n, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        mergeSort(S, n, left, mid)
        mergeSort(S, n, mid, right)
        merge(S, n, left, mid, right)

quickSort(A, 0, n-1)
mergeSort(S, n, 0, n)

def Judge():
    for _ in range(n):
        if A[_] != S[_]:
            return "Not stable"
    return "Stable"
    
print(Judge())
for _ in range(n):
    print(*A[_])
