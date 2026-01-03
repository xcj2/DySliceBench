
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n,k=getints()
values=getint2d(n)

k -= 1

values = list(sorted(values))
now = -1

for a,b in values:
    now_s = now + 1
    now_e = now + b
    if now_s <= k <= now_e:
        print(a)
        break
    now += b
