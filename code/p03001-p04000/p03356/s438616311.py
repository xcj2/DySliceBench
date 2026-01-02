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
        par[u] = v
    else:
        par[v] = u
        if rank[u] == rank[v]:
            rank[v] += 1

def same(u, v):
    u = root(u)
    v = root(v)
    if u == v:
        return 1
    return 0

N, M = map(int, input().split())
P = list(map(int, input().split()))
par = list(range(N))
rank = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    unite(x-1, y-1)

ans = 0
for i in range(N):
    ans += same(i, P[i] - 1)

print(ans)

