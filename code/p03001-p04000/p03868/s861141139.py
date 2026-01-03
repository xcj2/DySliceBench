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
    a = sorted([I() for _ in range(n)])
    b = sorted([I() for _ in range(n)])
    r = 1
    ai = 0
    bi = 0
    sa = 0
    while ai < n or bi < n:
        if ai >= n:
            if sa > 1:
                r *= sa
            sa -= 1
            bi += 1
        elif bi >= n:
            if sa < -1:
                r *= -sa
            sa += 1
            ai += 1
        elif a[ai] < b[bi]:
            if sa < -1:
                r *= -sa
            sa += 1
            ai += 1
        else:
            if sa > 1:
                r *= sa
            sa -= 1
            bi += 1
        r %= mod

    return r




print(main())

