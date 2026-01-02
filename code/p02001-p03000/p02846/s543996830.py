import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
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


def main():
    t1,t2 = LI()
    a1,a2 = LI()
    b1,b2 = LI()

    if a1 > b1:
        a1,b1 = b1,a1
        a2,b2 = b2,a2

    sa = t1*a1 + t2*a2
    sb = t1*b1 + t2*b2

    if sa == sb:
        return "infinity"

    if sb > sa:
        return 0

    t = t1*b1 - t1*a1
    st = sa - sb
    if t % st == 0:
        r = t // st * 2
    else:
        r = t // st * 2 + 1

    return r


print(main())



