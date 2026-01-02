def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r):
        if A[j][1] <= x:
            i = i + 1
            (A[i], A[j]) = (A[j], A[i])

    (A[i+1], A[r]) = (A[r], A[i+1])

    return i+1
    
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def stable(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            return "Not stable"
    return "Stable"

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = []
    R = []

    for i in range(n1):
        L.append(A[left+i])
    for i in range(n2):
        R.append(A[mid+i])

    L.append([0, 10**9])
    R.append([0, 10**9])

    i = 0
    j = 0

    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

n = int(input())
X = []
for i in range(n):
    a = input().split()
    X.append([a[0], int(a[1])])
    
Y = X[:]
quicksort(X, 0, n-1)
mergeSort(Y, 0, n)
print(stable(X, Y))
for elem in X:
    print(" ".join(map(str, elem)))

