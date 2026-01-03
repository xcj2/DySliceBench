
import collections
import itertools
import sys
import time

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

n,a=getints()
xs=getints()

def key(pos, s, c):
    return (pos * 2600 + s) * 55 + c

cache=[-1] * key(50, 2500, 50)

def solve(pos, s, c):
    if pos == n:
        if s == a * c and c:
            return 1
        else:
            return 0
    k = key(pos,s,c)
    res = cache[k]
    if res >= 0:
        return res
    res = 0
    res += solve(pos + 1, s + xs[pos], c + 1)
    res += solve(pos + 1, s, c)
    cache[k] = res
    return res

print(solve(0,0,0))