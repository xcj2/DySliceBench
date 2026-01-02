import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+100)
from collections import *

def bfs():
    q = deque([0])
    dep = [-1]*N
    dist = [-1]*N
    dep[0] = 0
    dist[0] = 0
    
    while q:
        v = q.popleft()
        
        for nv, _, w in G[v]:
            if dep[nv]==-1:
                parent[0][nv] = v
                dep[nv] = dep[v]+1
                dist[nv] = dist[v]+w
                q.append(nv)
    
    return dep, dist
    
def lca(u, v):
    if dep[u]>dep[v]:
        u, v = v, u
    
    for i in range(log_size):
        if ((dep[v]-dep[u])>>i)&1:
            v = parent[i][v]
    
    if u==v:
        return u
    
    for i in range(log_size-1, -1, -1):
        if parent[i][u]!=parent[i][v]:
            u, v = parent[i][u], parent[i][v]
    
    return parent[0][u]
    
def calc_dist(u, v):
    return dist[u]+dist[v]-2*dist[lca(u, v)]

def dfs(v, pv, now_cnt, now_wet):
    for c in cnt[v]:
        cnt[v][c] = now_cnt[c]
    
    for c in wet[v]:
        wet[v][c] = now_wet[c]
    
    for nv, c, w in G[v]:
        if nv==pv:
            continue
        
        now_cnt[c] += 1
        now_wet[c] += w
        dfs(nv, v, now_cnt, now_wet)
        now_cnt[c] -= 1
        now_wet[c] -= w

N, Q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b, c, d = map(int, input().split())
    G[a-1].append((b-1, c, d))
    G[b-1].append((a-1, c, d))
    
log_size = 20
parent = [[-1]*N for _ in range(log_size)]
dep, dist = bfs()

for i in range(1, log_size):
    for v in range(N):
        if parent[i-1][v]>=0:
            parent[i][v] = parent[i-1][parent[i-1][v]]

xyuv = [tuple(map(int, input().split())) for _ in range(Q)]
cnt = defaultdict(lambda: defaultdict(int))
wet = defaultdict(lambda: defaultdict(int))

for x, y, u, v in xyuv:
    cnt[u-1][x] = -1
    cnt[v-1][x] = -1
    cnt[lca(u-1, v-1)][x] = -1
    wet[u-1][x] = -1
    wet[v-1][x] = -1
    wet[lca(u-1, v-1)][x] = -1

dfs(0, -1, defaultdict(int), defaultdict(int))

for x, y, u, v in xyuv:
    l = lca(u-1, v-1)
    decr = wet[u-1][x]+wet[v-1][x]-2*wet[l][x]
    incr = y*(cnt[u-1][x]+cnt[v-1][x]-2*cnt[l][x])
    print(calc_dist(u-1, v-1)-decr+incr)