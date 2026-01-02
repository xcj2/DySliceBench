from operator import mul
from functools import reduce


def inpl():
    return list(map(int, input().split()))


def cmb(n, r):
    # combination
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def root(x):
    if parent[x] == x:
        return (x)
    else:
        parent[x] = root(parent[x])
        return (parent[x])


def same(x, y):
    return (root(x) == root(y))


def union(x, y):
    x = root(x)
    y = root(y)
    if (x == y):
        return False

    parent[x] = min(x, y)
    parent[y] = min(x, y)
    return True


N, M = inpl()
AB = [inpl() for _ in range(M)]
parent = [i for i in range(N)]
waku = [1] * N
anslist = [0] * M
ans = 0

for i, auau in enumerate(AB[::-1]):
    a = auau[0] - 1
    b = auau[1] - 1
    ra = root(a)
    rb = root(b)
    union(a, b)
    if ra != rb:
        ans -= cmb(waku[ra], 2) + cmb(waku[rb], 2)
        waku[root(a)] = waku[ra] + waku[rb]
        ans += cmb(waku[root(a)], 2)
    else:
        pass

    anslist[M - 1 - i] = ans

all_comb = cmb(N, 2)
for i in range(1, M):
    print(all_comb - anslist[i])
print(all_comb)
