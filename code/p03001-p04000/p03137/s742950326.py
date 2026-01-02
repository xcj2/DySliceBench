
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n,m=getints()
xs=getints()
xs=list(sorted(xs))

spaces=[]
for i in range(m-1):
    spaces.append(xs[i+1]-xs[i])

spaces = list(sorted(spaces))

for i in range(n-1):
    if spaces: spaces.pop()

print(sum(spaces))
