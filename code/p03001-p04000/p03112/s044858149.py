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
    a,b,q = LI()
    sa = [-inf,-inf] + [I() for _ in range(a)] + [inf, inf]
    ta = [-inf,-inf] + [I() for _ in range(b)] + [inf, inf]
    xa = [I() for _ in range(q)]
    r = []
    for x in xa:
        si = bisect.bisect_left(sa, x)
        ti = bisect.bisect_left(ta, x)
        l = sa[si-1]
        k = x - l
        ti2 = bisect.bisect_left(ta, l)
        t = inf
        if ti2 > 0 and t > k + l - ta[ti2-1]:
            t = k + l - ta[ti2-1]
        if t > k + ta[ti2] - l:
            t = k + ta[ti2] - l
        l = sa[si]
        k = l - x
        ti2 = bisect.bisect_left(ta, l)
        if ti2 > 0 and t > k + l - ta[ti2-1]:
            t = k + l - ta[ti2-1]
        if t > k + ta[ti2] - l:
            t = k + ta[ti2] - l

        l = ta[ti-1]
        k = x - l
        si2 = bisect.bisect_left(sa, l)
        if si2 > 0 and t > k + l - sa[si2-1]:
            t = k + l - sa[si2-1]
        if t > k + sa[si2] - l:
            t = k + sa[si2] - l
        l = ta[ti]
        k = l - x
        si2 = bisect.bisect_left(sa, l)
        if si2 > 0 and t > k + l - sa[si2-1]:
            t = k + l - sa[si2-1]
        if t > k + sa[si2] - l:
            t = k + sa[si2] - l


        r.append(t)

    return JA(r, "\n")

print(main())



