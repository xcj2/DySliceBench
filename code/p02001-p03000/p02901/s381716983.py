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
    n,m = LI()
    a = []
    c = []
    for i in range(m):
        d,b = LI()
        e = LI_()
        a.append(d)
        t = 0
        for u in e:
            t |= 2**u
        c.append(t)

    d = collections.defaultdict(lambda: inf)
    d[0] = 0
    for i in range(m):
        ai = a[i]
        ci = c[i]
        for k,v in list(d.items()):
            nk = k | ci
            nv = v + ai
            if d[nk] > nv:
                d[nk] = nv
    if d[2**n-1] == inf:
        return -1

    return d[2**n-1]


print(main())



