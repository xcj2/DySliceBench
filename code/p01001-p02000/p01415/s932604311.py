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
    n,k,t,u,v,l = LI()
    d = [I() for _ in range(n)] + [l]
    cd = ck = ct = 0
    r = 0
    for di in d:
        while ct < di and ck > 0:
            ct += t * v
            ck -= 1
        if ct >= di:
            r += (di - cd) / v
        else:
            r += (ct - cd) / v
            r += (di - ct) / u
            ct = di
        ck += 1
        if ck > k:
            ck = k
            ct = di + t * v
        cd = di

    return '{:0.9f}'.format(r)



print(main())

