import sys
sys.setrecursionlimit(10 ** 6)

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

N, M = map(int, input().split())
par = list(range(2 * N))
rank = [0] * (2 * N)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a, b + N)
    unite(a + N, b)

if same(0, N):
    print(N * (N - 1) // 2 - M)
else:
    c = 0
    for i in range(N):
        c += same(0, i)
    print(c * (N - c) - M)
