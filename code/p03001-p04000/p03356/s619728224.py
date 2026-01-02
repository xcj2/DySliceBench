import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def root(v):
    if v == par[v]:
        return v
    par[v] = root(par[v])
    return par[v]

def unite(u, v):
    u = root(u)
    v = root(v)
    if u == v:
        return
    if rank[u] < rank[v]:
        u, v = v, u
    par[v] = u
    if rank[u] == rank[v]:
        rank[u] += 1

def connected(u, v):
    return 1 if root(u) == root(v) else 0

N, M = map(int, input().split())
P = list(map(int, input().split()))
par = [i for i in range(N)]
rank = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    unite(x-1, y-1)
res = 0
for i in range(N):
    res += connected(i, P[i]-1)
print(res)
