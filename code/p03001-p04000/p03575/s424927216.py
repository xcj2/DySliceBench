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
            rank[u] += 1

def bridge(u, v):
    return root(u) != root(v)

N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]
ans = 0
for i in range(M):
    par = list(range(N))
    rank = [0] * N
    tmp_E = E[:i] + E[i+1:]
    for a, b in tmp_E:
        unite(a-1, b-1)
    a, b = E[i]
    ans += bridge(a-1, b-1)
print(ans)