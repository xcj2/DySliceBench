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
    n,W = LI()
    vw = [LI() for _ in range(n)]

    def rk(vw):
        r = collections.defaultdict(int)
        r[0] = 0
        for v,w in vw:
            rl = list(r.items())
            for rw,rv in rl:
                if rw + w > W:
                    continue
                if r[rw+w] < rv + v:
                    r[rw+w] = rv + v

        t = []
        m = -1
        for w,v in sorted(r.items()):
            if m < v:
                m = v
                t.append((w,v))

        return t

    r1 = rk(vw[:n//2])
    r2 = rk(vw[n//2:])

    i2 = len(r2) - 1
    r = 0
    for w,v in r1:
        while w + r2[i2][0] > W:
            i2 -= 1

        vv = v + r2[i2][1]
        if r < vv:
            r = vv

    return r

print(main())




