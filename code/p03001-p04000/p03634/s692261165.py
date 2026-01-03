import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline()[:-1]
from heapq import *

def dfs(s, es):
    dist = [None] * len(es)
    dist[s] = 0
    def ret(v, d):
        for u, c in es[v]:
            if dist[u] == None:
                dist[u] = dist[v] + c
                ret(u, dist[u])
    ret(s, 0)
    return dist
  
N = int(input())
es = [[] for i in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    es[a].append((b, c))
    es[b].append((a, c))
Q, K = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(Q)]
dist = dfs(K, es)
for i in range(Q):
    print(dist[xy[i][0]] + dist[xy[i][1]])
