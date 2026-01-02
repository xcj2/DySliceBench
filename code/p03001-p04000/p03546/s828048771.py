import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

H, W = mi()
C = li2(10)
A = li2(H)

## ワーシャルフロイド法
for k in range(10):
    for j in range(10):
        for i in range(10):
            C[i][j] = min(C[i][j], C[i][k]+C[k][j])

## 各要素における最小コストを合計
ans = 0
for i in range(H):
    for j in range(W):
        if abs(A[i][j]) != 1:
            ans += C[A[i][j]][1]

print(ans)