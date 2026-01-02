import sys

input = sys.stdin.buffer.readline
n, m = map(int, input().split())


# union-findを導入したい。
par = [-1] * (n + 10)


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
        False
    else:
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


for _ in range(m):
    a, b = map(int, input().split())
    unite(a, b)

num = 0
for i in range(n):
    num = max(num, size(i))
print(num)
