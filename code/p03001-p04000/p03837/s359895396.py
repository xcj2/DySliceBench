def warshall_floyd(n,d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

def examD():
    N, M = LI()
    D = [[float("inf") for i in range(N)] for i in range(N)]
    # d[u][v] : 辺uvのコスト(存在しないときはinf)
    XY = [[0,0]]*M
    for i in range(M):
        x, y, z = map(int, input().split())
        XY[i] = [x-1,y-1]
        D[x - 1][y - 1] = z
        D[y - 1][x - 1] = z
    for i in range(N):
        D[i][i] = 0  # 自身のところに行くコストは０
    d = copy.deepcopy(D)
#    print(warshall_floyd(N, d))
    W = warshall_floyd(N, d)
    cur = int(0)
    for i in range(M):
        if D[XY[i][0]][XY[i][1]]>W[XY[i][0]][XY[i][1]]:
            cur += 1
    print(cur)

import sys
import copy
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
