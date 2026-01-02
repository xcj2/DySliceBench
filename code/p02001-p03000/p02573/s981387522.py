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
    par[x] += par[y]
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
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a, b)
ans = -1 * min(par)

print(ans)
