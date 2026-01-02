def warshall_floyd(n,d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
##############################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N, M, L = LI()
d = [[float("inf") for i in range(N)] for i in range(N)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(M):
    x,y,z = map(int,input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(N):
    d[i][i] = 0 #自身のところに行くコストは０
#print(warshall_floyd(N,d))
cur = warshall_floyd(N,d)
newD = [[float("inf") for i in range(N)] for i in range(N)]
for i in range(N):
    for l,j in enumerate(cur[i]):
        if j<=L:
            newD[i][l] = 1
            newD[l][i]

ansC = warshall_floyd(N,newD)

Q = I()
for i in range(Q):
    s, t = LI()
    ans = ansC[s-1][t-1]-1
    if ans==inf:
        ans = -1
    print(ans)