
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n=getint()
hs=getints()

def solve(hs:list):
    if not hs or not max(hs):
        return 0
    add = min(hs)
    for i in range(len(hs)):
        hs[i] -= add
    res = add
    now = []
    for h in hs:
        if not h:
            res += solve(now)
            now = []
            continue
        now.append(h)
    res += solve(now)
    return res

print(solve(hs))
