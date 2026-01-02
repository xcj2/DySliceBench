import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]

K, N = mi()

A = li()

m = 0

for i in range(N-1):
    if A[i+1]-A[i] > m:
        m = A[i+1]-A[i]

if A[0]+(K-A[N-1]) > m:
    m = A[0]+(K-A[N-1])

print(K-m)