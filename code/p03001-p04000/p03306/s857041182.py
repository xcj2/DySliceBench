import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n,m = LI()
    a = [LI() for _ in range(m)]
    e = collections.defaultdict(list)
    for u,v,s in a:
        e[u].append((v,s))
        e[v].append((u,s))

    f = collections.defaultdict(bool)
    t = [None] * (n+1)
    t[e[1][0][0]] = -1000000
    nf = set()
    q = [e[1][0][0]]
    r = None
    while q:
        i = q.pop()
        for v,s in e[i]:
            if f[v]:
                continue
            if t[v] is None:
                t[v] = s - t[i]
                q.append(v)
            elif t[v] != s - t[i]:
                if v in nf:
                    return 0
                tv = (t[v] + s - t[i]) // 2
                t = [None] * (n+1)
                t[v] = tv
                nf.add(v)
                q = [v]
                break
        if nf:
            f = collections.defaultdict(bool)
        else:
            f[i] = True
    t[0] = inf
    t2 = t[:]
    tmi = t.index(min(t))
    f = collections.defaultdict(bool)
    t = [None] * (n+1)
    t[tmi] = 1
    nf = set()
    q = [tmi]
    r = None
    while q:
        i = q.pop()
        for v,s in e[i]:
            if f[v]:
                continue
            if t[v] is None:
                t[v] = s - t[i]
                q.append(v)
            elif t[v] != s - t[i]:
                if v in nf:
                    return 0
                tv = (t[v] + s - t[i]) // 2
                t = [None] * (n+1)
                t[v] = tv
                nf.add(v)
                q = [v]
                break
        if nf:
            f = collections.defaultdict(bool)
        else:
            f[i] = True
    r = inf
    if t[1:] == t2[1:]:
        if min(t[1:]) > 0:
            return 1
        return 0
    for i in range(1,n+1):
        if t[i] < 0:
            return 0
        if t[i] > t2[i]:
            continue
        if r > t[i]:
            r = t[i]


    return r



print(main())

