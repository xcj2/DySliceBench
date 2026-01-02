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
    rr = []
    M = 256
    sq = [i**2 for i in range(M)]
    nkss = [[sq[abs(x-nk)] for nk in range(M)] for x in range(M)]
    ML = list(range(M))

    def f(m, n):
        cs = [I() for _ in range(m)]
        xs = [I() for _ in range(n)]
        ml = list(range(m))
        d = [inf] * M
        nd = [inf] * M
        d[128] = 0
        ckl = list(map(lambda x: (max(min(x[0]+x[1], 255), 0), x[1]), (itertools.product(cs, ML))))
        for i in range(n):
            nd = [inf] * M
            for nk,k in ckl:
                if nd[nk] > d[k]:
                    nd[nk] = d[k]
            d = [nn + kk for nn,kk in zip(nd, nkss[xs[i]])]
        return min(d)

    while True:
        n,m = LI()
        if m == 0 and n == 0:
            break
        rr.append(f(m,n))

    return '\n'.join(map(str,rr))




print(main())

