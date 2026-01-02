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
    n,u,v = LI()
    ab = [LI() for _ in range(n-1)]
    e = collections.defaultdict(list)
    for a,b in ab:
        e[a].append(b)
        e[b].append(a)

    def search(s, ea):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        for u in ea:
            v[u] = True
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv in e[u]:
                if v[uv]:
                    continue
                vd = k + 1
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    du = search(u, [])
    dv = search(v, [])
    r = 0
    for i in range(n):
        if du[v] - du[u] < 3:
            break
        r += 1
        for c in e[u]:
            if dv[u] > dv[c]:
                u = c
                break
        for c in e[v]:
            if du[v] > du[c]:
                v = c
                break

    ea = []
    t = dv[u]
    for c in range(1, n+1):
        if dv[c] < t:
            ea.append(c)
    d = search(u, ea)
    m = max(d.values())
    r += m
    s = t - dv[v]
    if s > 1:
        r += 1

    return r


print(main())



