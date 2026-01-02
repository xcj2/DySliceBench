# Union-Find
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if par[x] > par[y]:
        x, y = y, x
    par[y] = x
    return True


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


N, M = map(int, input().split())
# 負のとき size, 非負のとき parent
par = [-1] * N
for i in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    unite(x, y)

print(par.count(-1))

