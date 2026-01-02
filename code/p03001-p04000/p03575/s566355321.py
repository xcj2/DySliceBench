import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()


upper = [0]

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

n, m = na()
es = []
for i in range(m):
    es.append(na())

ret = m
for i in range(m):
    upper = [-1] * n
    for j in range(m):
        if j != i:
            unite(es[j][0]-1, es[j][1]-1)
    for j in range(n):
        if upper[j] == -n:
            ret -= 1

print(ret)

