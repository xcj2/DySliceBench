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
    e = collections.defaultdict(set)
    f = collections.defaultdict(set)
    for _ in range(n+m-1):
        a,b = LI_()
        e[a].add(b)
        f[b].add(a)

    s = -1
    for k in e.keys():
        if len(f[k]) == 0:
            s = k
            break

    r = [None] * n
    r[s] = 0
    al = set([s])
    q = set([s])
    while q:
        u = set()
        for c in q:
            for d in e[c]:
                if len(f[d] - al) == 0:
                    u.add(d)
                    r[d] = c + 1
        al |= u
        q = u

    return '\n'.join(map(str, r))



print(main())


