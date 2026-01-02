import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    a = [[c for c in S()] for _ in range(n)]
    r = 0
    for i in range(n):
        b = [[a[ii][(j+i)%n] for j in range(n)] for ii in range(n)]
        f = True
        for ii in range(n):
            for jj in range(ii+1,n):
                if b[ii][jj] != b[jj][ii]:
                    f = False
                    break
            if not f:
                break
        if f:
            r += 1

    return r * n




print(main())

