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
    a = sorted([LI() for _ in range(n)], reverse=True)
    b = set([tuple(LI()) for _ in range(n)])
    r = 0
    for c in a:
        t = (-1, 10000)
        for d in b:
            if c[0] < d[0] and c[1] < d[1] and t[1] > d[1]:
                t = d
        if t != (-1, 10000):
            r += 1
            b.remove(t)

    return r


print(main())


