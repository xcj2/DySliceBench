def warshall_floyd(n,d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
######################################################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
mod = 10**9 + 7
inf = float('inf')
ans = int(0)
H, W = LI()
c = [LI() for _ in range(10)]
A = [LI() for _ in range(H)]
d = [[float("inf") for i in range(10)] for i in range(10)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(10):
    for j in range(10):
        d[i][j] = c[i][j]
for i in range(10):
    d[i][i] = 0 #自身のところに行くコストは０
#print(warshall_floyd(10,d))
L = warshall_floyd(10,d)
cur = int(0)
for i in range(H):
    for j in range(W):
        l = A[i][j]
        if l>=0:
            cur += L[l][1]

ans = cur
print(ans)
