
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n=input()
s=input()

l,r=0,0
for c in s:
    if c == '(':
        r += 1
    else:
        if r:
            r -= 1
        else:
            l += 1
res = "(" * l + s + ")" * r
print(res)