
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
p = list(range(n))
r = [1] * n


def li_(): return [int(x)-1 for x in sys.stdin.readline().split()]


def find(x):
    global p
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    x, y = find(x), find(y)
    if y > x:
        x, y = y, x
    p[y] = x
    r[x] += r[y]
    r[y] = r[x]


flist = [0] * m
elist = [0] * m
for i in range(m):
    flist[i], elist[i] = li_()

flist.reverse()
elist.reverse()

ans = [0] * m
ans[-1] = int(n*(n-1)/2)

for i in range(m-1):
    a, b = flist[i], elist[i]
    if find(a) != find(b):
        ans[-i-2] = ans[-i-1] - r[find(a)]*r[find(b)]
        union(a, b)
    else:
        ans[-i-2] = ans[-i-1]
    if ans[-i-2] == 0:
        break

for i in range(m):
    print(ans[i])
