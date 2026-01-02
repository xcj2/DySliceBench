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
    n = I()
    lr = sorted([LI() for _ in range(n)])
    la = [x[0] for x in lr]
    ra = sorted([x[1] for x in lr])

    rr = 0
    for l, r in lr:
        t = r - l + 1
        tl = la[-1]
        if l == tl:
            tl = la[-2]
        tr = ra[0]
        if r == tr:
            tr = ra[1]
        if tr >= tl:
            t += tr - tl + 1
        if rr < t:
            rr = t

    mr = [lr[0][1]]
    for _, r in lr[1:]:
        if mr[-1] > r:
            mr.append(r)
        else:
            mr.append(mr[-1])

    tl, tr = lr[-1]
    for i in range(n-2, 0, -1):
        r = lr[i][1]
        if tr > r:
            tr = r
        if tr < tl:
            break
        if mr[i-1] < lr[i-1][0]:
            continue
        t = tr - tl + 1 + mr[i-1] - lr[i-1][0] + 1
        if rr < t:
            rr = t

    return rr

print(main())



