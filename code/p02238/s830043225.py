import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

N = I()
adj = [[] for _ in range(N)]
visited = [False for _ in range(N)]
d = [0 for _ in range(N)]
f = [0 for _ in range(N)]
cur_time = 1

for _ in range(N):
    edge_list = LI()
    u, k = edge_list[0], edge_list[1]
    if k == 0:
        continue
    v_list = edge_list[2:]
    u -= 1
    for v in v_list:
        v -= 1
        adj[u].append(v)

def dfs(u):
    global cur_time
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            d[v] = cur_time
            cur_time += 1
            dfs(v)
    f[u] = cur_time
    cur_time += 1
    return

for v in range(N):
    if not visited[v]:
        d[v] = cur_time
        cur_time += 1
        dfs(v)

for v in range(N):
    print(v+1, d[v], f[v])



