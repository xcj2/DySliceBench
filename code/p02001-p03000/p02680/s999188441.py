import sys

sys.setrecursionlimit(500005)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n, m = na()

hors = []
for i in range(n):
    hors.append(na())
vers = []
for j in range(m):
    vers.append(na())

xs = set()
for hor in hors:
    xs.add(hor[0])
    xs.add(hor[1])
for ver in vers:
    xs.add(ver[0])

xs = list(xs)
xs.sort()


ys = set()
for hor in hors:
    ys.add(hor[2])
for ver in vers:
    ys.add(ver[1])
    ys.add(ver[2])

ys = list(ys)
ys.sort()

upper = [-1] * ((len(xs)+1)*(len(ys)+1))
H = len(ys)+1

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

import bisect
horb = [[0] * (len(xs)+1) for _ in range(len(ys))]
for hor in hors:
    y = bisect.bisect_left(ys, hor[2])
    horb[y][bisect.bisect_left(xs, hor[0])] += 1
    horb[y][bisect.bisect_left(xs, hor[1])] -= 1
for i in range(len(ys)):
    for j in range(1, len(xs)+1):
        horb[i][j] += horb[i][j-1]

verb = [[0] * (len(ys)+1) for _ in range(len(xs))]
for ver in vers:
    x = bisect.bisect_left(xs, ver[0])
    verb[x][bisect.bisect_left(ys, ver[1])] += 1
    verb[x][bisect.bisect_left(ys, ver[2])] -= 1
for i in range(len(xs)):
    for j in range(1, len(ys)+1):
        verb[i][j] += verb[i][j-1]

for i in range(len(xs)+1):
    for j in range(len(ys)+1):
        if i < len(xs) and j in (0, len(ys)):
            # print(i, j, i+1, j)
            unite(i*H+j, (i+1)*H+j)
        elif i < len(xs) and verb[i][j-1] == 0:
            # print(i, j, i+1, j)
            unite(i*H+j, (i+1)*H+j)
        if j < len(ys) and i in (0, len(xs)):
            # print(i, j, i, j+1)
            unite(i*H+j, i*H+j+1)
        elif j < len(ys) and horb[j][i-1] == 0:
            # print(i, j, i, j+1)
            unite(i*H+j, i*H+j+1)

ox = bisect.bisect_left(xs, 0)
oy = bisect.bisect_left(ys, 0)

if equiv(ox*H+oy, 0):
    print("INF")
else:
    S = 0
    for i in range(len(xs) + 1):
        for j in range(len(ys) + 1):
            if equiv(i*H+j, ox*H+oy):
                S += (xs[i] - xs[i-1]) * (ys[j] - ys[j-1])
    print(S)
