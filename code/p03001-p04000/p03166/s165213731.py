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
    for _ in range(m):
        x,y = LI()
        e[y].add(x)

    fm = {}
    def f(i):
        if i in fm:
            return fm[i]
        if len(e[i]) == 0:
            fm[i] = 0
            return 0
        r = 0
        for c in e[i]:
            t = f(c)
            if r < t:
                r = t
        fm[i] = r + 1
        return r + 1

    r = 0
    for i in range(1,n+1):
        t = f(i)
        if r < t:
            r = t

    return r


print(main())
