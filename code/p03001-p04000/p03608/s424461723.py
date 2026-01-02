def warshall_floyd(n,d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
##################################################################
import itertools
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')

N, M, R = LI()
r = LI()
cur = 0
ans = inf
d = [[float("inf") for i in range(N)] for i in range(N)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(M):
    x,y,z = map(int,input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(N):
    d[i][i] = 0 #自身のところに行くコストは０
#print(warshall_floyd(N,d))
W = warshall_floyd(N,d)
loop = int(1)
#for i in range(len(r)):
#    loop *=(i+1)
for course in itertools.permutations(r):
    cur = int(0)
    for i in range(len(course)-1):
        to = course[i+1]
        go = course[i]
        cur += W[go-1][to-1]
    ans = min(ans,cur)

print(ans)