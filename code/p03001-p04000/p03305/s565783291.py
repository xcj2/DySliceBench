def dijkstra_heap(n,s,edge,k):
    # 始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n  # True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heappush(edgelist, [e[k],e[2]])
    while edgelist:
        minedge = heappop(edgelist)
        # まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[2]]:
                heappush(edgelist, [e[k] + d[v], e[2]])
    return d

def examD():
    N, M, s, t = LI()
    edge = defaultdict(list)
#    edge2 = defaultdict(list)
    # edge2 メモリ無駄
    for i in range(M):
        x, y, z1, z2 = map(int, input().split())
        x -=1; y -=1
        edge[x].append((z1,z2,y))
        edge[y].append((z1,z2,x))
    start1 = s-1
    start2 = t-1
    res1 = dijkstra_heap(N,start1, edge,0)
    res2 = dijkstra_heap(N,start2, edge,1)
    ans = []
    snuke = 10**15
    cur = res1[N-1] + res2[N-1]
    ans.append(snuke-cur)
    for i in range(N-2,-1,-1):
        if res1[i] + res2[i]<cur:
            cur = res1[i] + res2[i]
            ans.append(snuke-cur)
        else:
            ans.append(snuke-cur)
    for v in ans[::-1]:
        print(v)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
