from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def dijkstra_heap(s):
    #始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heappush(edgelist,e)
    while len(edgelist):
        minedge = heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heappush(edgelist,[e[0]+d[v],e[1]])
    return d

################################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(w):
    x,y,z = map(int,input().split())
    edge[x-1].append([z,y-1])
for i in range(n-1):
    edge[i+1].append([0,i])
res = dijkstra_heap(0)
if res[-1] == float('inf'):
    print(-1)
else:
    print(res[-1])