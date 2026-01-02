import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def inv(x):
    return pow(x, mod - 2, mod)

def comb(n, b):
    if b > n - b:
        b = n - b
    r = 1
    for k in range(n, n-b, -1):
        r = r * k % mod
    d = 1
    for k in range(1, b+1):
        d = d * k % mod
    return r * inv(d) % mod

def main():
    x,y = LI()
    x,y = max(x,y), min(x,y)
    if (x+y) % 3 > 0 or x > y*2:
        return 0

    c = (x+y) // 3
    xc = (x-y) + (c - (x-y)) // 2

    return comb(c,xc)


print(main())


