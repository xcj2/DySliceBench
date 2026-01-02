import sys
input = sys.stdin.readline
cnt = 0

def Merge(As, Ms, l, m, r):
    global cnt
    cnt += r - l
    L = As[l:m] + [float('inf')]
    R = As[m:r] + [float('inf')]
    Lm = Ms[l:m]
    Rm = Ms[m:r]
    i, j = 0, 0
    for k in range(l, r):
        if L[i] <= R[j]:
            As[k] = L[i]
            Ms[k] = Lm[i]
            i += 1
        else:
            As[k] = R[j]
            Ms[k] = Rm[j]
            j += 1
    return

def MergeSort(As, Ms, l, r):
    if r - l > 1:
        m = (l + r) // 2
        MergeSort(As, Ms, l, m)
        MergeSort(As, Ms, m, r)
        Merge(As, Ms, l, m, r)
    return

def Partition(A, p, r):
    i = p - 1
    for j in range(p, r):
        if A[j] <= A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
            M[i], M[j] = M[j], M[i]
    A[i+1], A[r] = A[r], A[i+1]
    M[i+1], M[r] = M[r], M[i+1]
    return i+1

def QuickSort(A, p, r):
    if p < r:
        m = Partition(A, p, r)
        QuickSort(A, p, m-1)
        QuickSort(A, m+1, r)

n = int(input())
M, A = [], []
for i in range(n):
    a, b = input().split()
    M.append(a)
    A.append(int(b))
As = A[:]
Ms = M[:]
QuickSort(A, 0, n-1)
MergeSort(As, Ms, 0, n)
if M == Ms:
    print('Stable')
else:
    print('Not stable')
for i in range(n):
    print('{} {}'.format(M[i], A[i]))
