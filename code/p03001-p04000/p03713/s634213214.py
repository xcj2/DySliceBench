
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

h,w=getints()

def solve2(h,w):
    if h % 2 == 0:
        e = h // 2 * w
        return (e,e)
    if w % 2 == 0:
        e = h * w // 2
        return (e,e)
    h1 = h // 2
    h2 = h - h1
    e1 = (h1 * w, h2 * w)
    w1 = w // 2
    w2 = w - w1
    e2 = (h * w1, h * w2)
    return e2 if abs(e2[0] - e2[1]) < abs(e1[0] - e1[1]) else e1

def solve3():
    res = h * w
    for i in range(1, h):
        m = i * w
        r = solve2(h-i,w)
        values = list(sorted([m, r[0], r[1]]))
        res = min(res, values[2] - values[0])
    for j in range(1, w):
        m = h * j
        r = solve2(h, w - j)
        values = list(sorted([m, r[0], r[1]]))
        res = min(res, values[2] - values[0])
    return res

print(solve3())
