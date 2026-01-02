n, m = map(int, input().split())
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(m)]

par = [i for i in range(n)]
rank = [1 for _ in range(n)]


def root(x):
    if x == par[x]:
        return x
    par[x] = root(par[x])
    return par[x]


def is_same(x, y):
    return root(x) == root(y)


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    par[x] = y


for x, y in xy:
    unite(x - 1, y - 1)


count = 0
for i, p_i in enumerate(p):
    count += 1 if is_same(i, p_i - 1) else 0
print(count)
