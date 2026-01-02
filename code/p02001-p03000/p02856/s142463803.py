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
    m = I()
    aa = [LI() for _ in range(m)]
    r = 0
    cc = collections.defaultdict(int)
    for d,c in aa:
        cc[d] += c
    f = True
    r = 0
    v = []
    for i in range(10):
        s = str(i * 2)
        t = []
        for c in s:
            t.append(int(c))
        v.append(t)

    r = 0
    while f:
        f = False
        for i in range(1,10):
            t = cc[i]
            if t > 1:
                cc[i] = t % 2
                r += t // 2
                for c in v[i]:
                    cc[c] += t // 2
                f = True
    a = []
    for i,c in cc.items():
        if i == 0:
            r += c
        elif c > 0:
            a.append(i)

    t = a[0]
    for c in a[1:]:
        r += 1
        t += c
        while t > 9:
            r += 1
            t = t//10 + t%10

    return r


print(main())



