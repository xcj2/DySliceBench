
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
values = list(sorted(getints()))

mx = max(values)
idx1 = bisect.bisect_left(values, mx // 2)
idx2 = idx1 - 1 if idx1 > 0 else idx1

if abs(mx - values[idx1] * 2) < abs(mx - values[idx2] * 2):
    idx = idx1
else:
    idx = idx2

print(mx, values[idx])