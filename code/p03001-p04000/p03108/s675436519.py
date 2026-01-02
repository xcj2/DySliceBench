n, m = map(int, input().split())

par = [-1] * (n + 1)


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def size(x):
    X = find(x)
    return -par[X]


def unite(x, y):
    if find(x) == find(y):
        return False
    X = find(x)
    Y = find(y)
    if size(X) < size(Y):
        x, y = y, x
        X = find(x)
        Y = find(y)
    par[X] += par[Y]
    par[Y] = X
    return True


def is_same(x, y):
    return find(x) == find(y)


def calc(a):
    return a * (a - 1) // 2


goukei = calc(n)
ans = [-1] * (m + 1)
ans[-1] = calc(n)
cnt = 0
AB = [list(map(int, input().split())) for _ in range(m)]
for i in range(m - 1, -1, -1):
    a, b = AB[i]
    if is_same(a, b):
        ans[i] = goukei - cnt
    else:
        A = size(a)
        B = size(b)
        cnt += calc(A + B) - calc(A) - calc(B)
        unite(a, b)
        ans[i] = goukei - cnt
print(*ans[1::], sep="\n")
