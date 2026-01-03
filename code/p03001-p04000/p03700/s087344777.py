
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n,a,b=getints()
hs=[getint() for _ in range(n)]
mx=max(hs)

min_cast = 0
max_cast = mx+1
c = a-b

hs = list(sorted(hs,reverse=True))

while min_cast < max_cast:
    cast = (min_cast + max_cast) // 2
    #values= list(filter(lambda s: s > 0, map(lambda s: s - b*cast, hs)))
    #need = sum(map(lambda v: (v + c - 1) // c, values))
    need = 0
    dec = b * cast
    for v in hs:
        v = v - dec
        if v <= 0:
            break
        need += (v + c - 1) // c
    if need <= cast:
        max_cast = cast
    else:
        min_cast = cast + 1

print(min_cast)