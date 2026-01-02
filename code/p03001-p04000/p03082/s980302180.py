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
    n,x = LI()
    a = sorted(LI(),reverse=True)
    d = collections.defaultdict(int)
    d[x] = 1
    for i in range(n):
        c = a[i]
        e = collections.defaultdict(int)
        for k,v in d.items():
            e[k] += v * (n-i-1)
            e[k] %= mod
            e[k%c] += v
            e[k%c] %= mod

        d = e

    r = 0
    for k,v in d.items():
        r += k * v
        r %= mod

    return r


print(main())


