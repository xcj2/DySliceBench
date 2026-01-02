
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

hs[0] -= 1
ok = True
for i in range(1, n):
    if hs[i] > hs[i - 1]:
        hs[i] -= 1
    if hs[i] < hs[i - 1]:
        ok = False

print("Yes" if ok else "No")
