import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()
cnt = 0
#bubbleSort(A, N)
flag = 1
while flag:
    flag = 0
    for i in range(N - 1, 0, -1):
        if A[i] < A[i - 1]:
            a = A[i]
            b = A[i - 1]
            A[i] = b
            A[i - 1] = a
            flag = 1
            cnt += 1
print(' '.join(map(str, A)))
print(cnt)
