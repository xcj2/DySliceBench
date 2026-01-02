import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import random

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


def main():
    n = I()
    s = S()
    aa = [LI_() for _ in range(n-1)]
    e = collections.defaultdict(set)
    for a,b in aa:
        e[a].add(b)
        e[b].add(a)

    sa = []
    for i in range(n):
        if s[i] == '1':
            sa.append(i)

    if len(sa) <= 1:
        return 0

    m = {}
    def f(i,p):
        k = (i,p)
        if k in m:
            return m[k]

        t = 0
        if s[i] == '1':
            t = 1

        h = []
        tk = 0
        tc = 0
        for c in e[i]:
            if c == p:
                continue
            r = f(c,i)
            if r[0] < 1:
                continue
            tc += r[0]
            tk += r[0] + r[1]
            h.append([r[0]+r[1],r[2]])

        if p == -1:
            return h

        mk = 0
        mv = 0
        for u,v in h:
            if mk < u:
                mk = u
                mv = v
        if mk > tk - mk:
            kk = tk - mk
            mk -= kk
            kk += min(mv//2,mk)
            m[k] = (tc+t,tk,kk*2)
        else:
            m[k] = (tc+t,tk,tk//2*2)

        return m[k]

    r = inf

    for i in range(n):
        t = f(i,-1)
        tk = 0
        mk = 0
        for u,v in t:
            tk += u
        if tk % 2 == 1:
            continue

        ff = 1
        for u,v in t:
            kk = u-v
            nk = tk - u
            if kk > nk:
                ff = 0
        # print(i,ff,tk,mk,t)
        if ff == 0:
            continue
        if tk // 2 < mk:
            continue
        v = tk // 2
        if r > v:
            r = v

    if r == inf:
        return -1

    return r


print(main())

