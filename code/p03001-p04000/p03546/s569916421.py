def dijkstra_heap(n,s,edge):
    # 始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n  # True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heappush(edgelist, e)
    while len(edgelist):
        minedge = heappop(edgelist)
        # まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heappush(edgelist, [e[0] + d[v], e[1]])
    return d
def examD():
    H, W = LI()
    c = [LI() for _ in range(10)]
    A = [LI() for _ in range(H)]
    edge = [[] for i in range(10)]
    # edge[i] : iから出る道の[重み,行先]の配列
    for i in range(10):
        for j in range(10):
            x, y, z = i, j, c[i][j]
            edge[x].append([z, y])
    res = []
    for i in range(10):
        res.append(dijkstra_heap(10, i, edge))
#    print(res)
    d = defaultdict(int)
    for l in A:
        for j in l:
            d[j] +=1
    ans = 0
    for i in range(10):
        ans += d[i]*res[i][1]
    print(ans)

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
