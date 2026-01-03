
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n = getint()
points = [getint() for _ in range(n)]

cache = {}

def solve(pos, modulo):

    key = (pos, modulo)
    if key in cache:
        return cache[key]

    if pos == n:
        return -100000000 if modulo == 0 else 0

    res1 = solve(pos + 1, modulo)
    res2 = solve(pos + 1, (modulo + points[pos]) % 10) + points[pos]

    res = max(res1, res2)
    cache[key] = res

    return res

res = max(solve(0, 0), 0)

print(res)