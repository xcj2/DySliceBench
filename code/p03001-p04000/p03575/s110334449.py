import copy

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
Road = [tuple(map(int, input().split())) for _ in range(M)]
ans = 0
for i in range(M):
    Roadi = copy.deepcopy(Road)
    par = [-1] * N
    for j, r in enumerate(Road):
        if i == j:
            continue
        ra, rb = r
        ra -= 1
        rb -= 1
        unite(ra, rb)
    if par.count(-1) > 1:
        ans += 1

print(ans)