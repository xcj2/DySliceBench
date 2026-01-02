import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LS()
A_Bub = []
A_Sel = []
for i in range(N):
    A_Bub.append([A[i][0], int(A[i][1]), i])
    A_Sel.append([A[i][0], int(A[i][1]), i])

#BubleSort(C, N)
def BubleSort(C, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if C[j][1] < C[j - 1][1]:
                a = C[j]
                b = C[j - 1]
                C[j] = b
                C[j - 1] = a

#SelectionSort(C, N)
def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        a = C[i]
        b = C[minj]
        C[i] = b
        C[minj] = a

def Check(C, N):
    for i in range(1, N):
        if C[i][1] == C[i - 1][1]:
            if C[i][2] < C[i - 1][2]:
                return 'Not stable'
    return 'Stable'
BubleSort(A_Bub, N)
ans_Bub = []
for i in range(N):
    b = [A_Bub[i][0], A_Bub[i][1]]
    ans_Bub.append(''.join(map(str, b)))
print(' '.join(map(str, ans_Bub)))
print(Check(A_Bub, N))


SelectionSort(A_Sel, N)
ans_Sel = []
for i in range(N):
    s = [A_Sel[i][0], A_Sel[i][1]]
    ans_Sel.append(''.join(map(str, s)))
print(' '.join(map(str, ans_Sel)))
print(Check(A_Sel, N))
