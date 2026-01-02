import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
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
    f = [LI() for _ in range(n)]
    p = [LI() for _ in range(n)]
    ii = [2**_ for _ in range(10)]
    r = -inf
    for k in range(1,2**10):
        a = [0] * n
        for i in range(10):
            if k&ii[i]:
                for j in range(n):
                    if f[j][i] == 1:
                        a[j] += 1
        tr = 0
        for i in range(n):
            tr += p[i][a[i]]
        if r < tr:
            r = tr

    return r



print(main())


