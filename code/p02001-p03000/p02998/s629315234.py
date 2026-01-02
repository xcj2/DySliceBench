import sys
from bisect import bisect_left

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()

upper = [-1]*(2*n)
nxs = [0]*(2*n)
for i in range(n):
    nxs[i] += 1

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
        nxs[x] += nxs[y]
        upper[y] = x
    return x == y



co = []

for i in range(n):
    co.append(na())

xs = list(set(_[0] for _ in co))
xs.sort()

ys = list(set(_[1] for _ in co))
ys.sort()

for c in co:
    unite(bisect_left(xs, c[0]), bisect_left(ys, c[1])+n)

ans = 0
for i in range(2*n):
    if upper[i] < 0:
        ans += nxs[i] * (-upper[i] - nxs[i])
ans -= n
print(ans)
