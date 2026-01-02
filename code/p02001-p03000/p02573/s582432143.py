n, m = map(int, input().split())
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def unite(x, y):
    p = find(x)
    q = find(y)
    if p == q:
        return None
    if p > q:
        p,q = q,p
    par[p] += par[q]
    par[q] = p
def same(x, y):
    return find(x) == find(y)
def size(x):
    return -par[find(x)]
par = [-1 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    unite(a - 1, b - 1)
ans = 0
for i in range(n):
    ans = max(ans, size(i))
print(ans)