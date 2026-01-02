def root(v):
    if par[v] == v:
        return v
    r = root(par[v])
    diff_weight[v] += diff_weight[par[v]]
    par[v] = r
    return r

def weight(v):
    root(v)
    return diff_weight[v]

def diff(u, v):
    return weight(v) - weight(u)

def unite(u, v, w):
    w += diff(v, u)
    u = root(u)
    v = root(v)
    if u == v:
        return
    if rank[u] < rank[v]:
        u, v = v, u
        w = -w
    par[v] = u
    diff_weight[v] = w
    if rank[u] == rank[v]:
        rank[u] += 1

def same(u, v):
    return root(u) == root(v)

N, M = map(int, input().split())
par = list(range(N))
rank = [0] * N
diff_weight = [0] * N
for _ in range(M):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    if same(l, r):
        dist = diff(l, r)
        if dist != d:
            print("No")
            exit()
    else:
        unite(l, r, d)

print("Yes")