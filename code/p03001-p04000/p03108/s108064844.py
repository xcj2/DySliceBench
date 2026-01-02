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
Bridge = [tuple(map(int, input().split())) for _ in range(M)]
Bridge = Bridge[::-1]
Ans = []
ans = N * (N-1) // 2
for (a, b) in Bridge:
    Ans.append(ans)
    if find(a-1) != find(b-1):
        x = size(a-1)
        y = size(b-1)
    else:
        x = 0
        y = 0
    unite(a-1, b-1)
    ans -= x * y


Ans = Ans[::-1]

for an in Ans:
    print(an)

