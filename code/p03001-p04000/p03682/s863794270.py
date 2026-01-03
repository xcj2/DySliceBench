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

def same(u, v):
    return root(u) == root(v)

def kruskal(edges):
    heapq.heapify(edges)
    res = 0
    while edges:
        w, u, v = heapq.heappop(edges)
        if same(u, v):
            continue
        unite(u, v)
        res += w
    return res

import heapq
N = int(input())
X = [() for _ in range(N)]
Y = [() for _ in range(N)]
for i in range(N):
    x, y = map(int, input().split())
    X[i] = (x, i)
    Y[i] = (y, i)
X = sorted(X)
Y = sorted(Y)
E = []
heapq.heapify(E)
for i in range(N-1):
    x, v = X[i]
    nx, nv = X[i+1]
    heapq.heappush(E, (nx-x, v, nv))
    y, u = Y[i]
    ny, nu = Y[i+1]
    heapq.heappush(E, (ny-y, u, nu))

par = list(range(N))
rank = [0] * N
print(kruskal(E))