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
    a = LI()
    b = LI()
    g = collections.defaultdict(int)
    h = collections.defaultdict(int)
    for d in a:
        for e in b:
            if d == e:
                g[d] += 1
                if g[d] > 1:
                    return 0
                continue
            if d < e:
                h[d] += 1
            else:
                h[e] += 1

    r = 1
    for d in a:
        if d in b:
            continue
        c = 0
        for e in b:
            if e > d:
                c += 1
        if c == 0:
            return 0
        r *= c
        h[d] -= 1
        g[d] = 1

    for e in b:
        if e in a:
            continue
        c = 0
        for d in a:
            if d > e:
                c += 1
        if c == 0:
            return 0
        r *= c
        h[e] -= 1
        g[e] = 1

    c = 0
    for i in range(n*m,0,-1):
        c += h[i]
        if g[i] == 1:
            continue
        if c == 0:
            return 0
        r *= c
        r %= mod
        c -= 1

    return r


print(main())



