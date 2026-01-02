import sys

sys.setrecursionlimit(500005)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()



n, m = na()

upper = [-1] * n
def root(x):
    if upper[x] < 0:
        return x
    else:
        upper[x] = root(upper[x])
        return upper[x]

def equiv(x, y):
    return root(x) == root(y)

def unite(x, y):
    x, y = root(x), root(y)
    if x != y:
        if upper[y] < upper[x]:
            x, y = y, x
        upper[x] += upper[y]
        upper[y] = x
    return x == y

for i in range(m):
    a, b = na()
    unite(a-1, b-1)

print(-min(upper))
