n, m = map(int, input().split())
P = list(map(int, input().split()))

# union-Find##
par = [-1] * (n + 1)


def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]


def unite(x, y):
    a = root(x)
    b = root(y)
    if a == b:
        return False
    else:
        if par[a] > par[b]:
            a, b = b, a
        par[a] += par[b]
        par[b] = a
        return True


def is_same(x, y):
    return root(x) == root(y)


def size(x):
    return -par[root(x)]


# union-find##

for _ in range(m):
    x, y = map(int, input().split())
    unite(x, y)

cnt = 0
for i in range(n):
    if is_same(P[i], i + 1):
        cnt += 1
print(cnt)
