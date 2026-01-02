def partition(A, p, r):
    x = A[r][1]
    i = p - 2
    for j in range(p-1, r):
        if A[j][1] <= x:
            i = i + 1
            hoge = A[i]
            A[i] = A[j]
            A[j] = hoge
    hoge = A[i+1]
    A[i+1] = A[r]
    A[r] = hoge
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
        
    return

def isStable(inData, outData, N):
    for i in range(N):
        if inData[i][0] != outData[i][0]:
            return False
    return True

def merge(A, left, mid, right):

    n1 = mid - left
    n2 = right - mid
    
    L = list(range(n1+1))
    R = list(range(n2+1))
    
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
        
    L[n1] = ['ban', 100000000000]
    R[n2] = ['ban', 100000000000]
    
    i = 0
    j = 0
    
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i = i + 1
            
        else:
            A[k] = R[j]
            j = j + 1
            
    return
            
def mergeSort(A, left, right):
    count = 0
    if left+1 < right:
        mid = int((left + right) / 2)
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

    return


import sys
import copy

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    tin = list(sys.stdin.readline().split())
    a.append([tin[0], int(tin[1])])
b = copy.deepcopy(a)

key = quickSort(a, 1, n -1)
mergeSort(b, 0, n)

if isStable(a, b, n):
    print('Stable')
else:
    print('Not stable')

for _ in range(n):
    print(*a[_])

