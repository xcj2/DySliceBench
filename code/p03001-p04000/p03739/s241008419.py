
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
values = getints()

def solve(values, prev):
    res = 0
    for v in values:
        s = prev + v
        add = 0
        if prev > 0 and s >= 0:
            add = -s - 1
        if prev < 0 and s <= 0:
            add = -s + 1
        res += abs(add)
        prev = s + add
    return res

res1, res2 = 0, 0
if values[0] <= 0:
    add = abs(values[0]) + 1
    res1 = solve(values[1:], values[0] + add) + abs(add)
    add = -1 if values[0] == 0 else 0
    res2 = solve(values[1:], values[0] + add) + abs(add)
else:
    add = 1 if values[0] == 0 else 0
    res1 = solve(values[1:], values[0] + add) + abs(add)
    add = -(values[0] + 1)
    res2 = solve(values[1:], values[0] + add) + abs(add)

print(min(res1, res2))
