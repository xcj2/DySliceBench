n, m = map(int, input().split())
x = [0] + list(map(int, input().split()))
e =  [tuple(map(int, input().split())) for i in range(m)]
e = sorted((w, u, v) for u, v, w in e)

p, r, bad = list(range(n + 1)), [0] * (n + 1), [0] * (n + 1)
wt = x[:]

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y, w):
    x, y = find(x), find(y)
    if r[x] < r[y]: x, y = y, x
    p[y] = x
    r[x] += r[x] == r[y]
    wt[x] += wt[y]
    bad[x] += bad[y]
    if wt[x] < w:
        bad[x] += 1
    else:
        bad[x] = 0

def add(x, w):
    x = find(x)
    if wt[x] < w:
        bad[x] += 1

for w, u, v in e:
    if find(u) == find(v):
        add(u, w)
    else:
        union(u, v, w)

ans = 0
for u in range(1, n + 1):
    if p[u] == u: ans += bad[u]

print(ans)
