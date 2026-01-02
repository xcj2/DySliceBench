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

def bs(f, mi, ma):
    mm = -1
    while ma > mi:
        mm = (ma+mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm

def main():
    n,m = LI()
    a = sorted(LI(), reverse=True)
    t = a[0]
    r = [0] * (t*2+1)
    u = [0] * (t*2+1)
    for c in a:
        r[c] += 1
        u[c] += c

    for i in range(t-1,-1,-1):
        r[i] += r[i+1]
        u[i] += u[i+1]

    def f(i):
        t = 0
        for c in a:
            if c >= i:
                t += n
            else:
                t += r[i-c]
        return t >= m

    i1 = bs(f,0,t*2+1) - 1

    rr = 0
    k = 0
    for c in a:
        ci = max(i1-c,0)
        ac = r[ci]
        if ac == 0:
            continue
        rr += u[ci]
        rr += c * ac
        k += ac

    rr -= (k-m) * i1

    return rr


print(main())


