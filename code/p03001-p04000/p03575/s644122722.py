# なぜかunion findが動かないので手癖で復習
n, m = map(int, input().split())
# par = [i for i in range(n)]

def root(x, par):
    if x == par[x]:
        return x
    else:
        t = root(par[x], par)
        par[x] = t
        return t

def same(a, b, par):
    return root(a, par) == root(b, par)

def union(a, b, par):
    if not same(a, b, par):
        ra = root(a, par)
        rb = root(b, par)
        # par[rb] = ra
        par[rb] = a

edges = []
for _ in range(m):
    edges.append(tuple(map(lambda x : int(x)-1, input().split())))

ans = 0
for i in range(m):
    par = [k for k in range(n)]
    for j in range(m):
        if i == j:
            continue
        a, b = edges[j]
        if same(a, b, par):
            continue
        union(a, b, par)
    # 以降が.....
    a, b = edges[i]
    if not same(a, b, par):
        ans += 1
print(ans)