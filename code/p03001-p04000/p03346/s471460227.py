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
    d = {}
    d[0] = -1
    for i in range(n):
        d[I()] = i
    r = n - 1
    c = 0
    for i in range(1,n+1):
        if d[i-1] > d[i]:
            if r > n - c:
                r = n - c
            c = 1
        else:
            c += 1
    if r > n - c:
        r = n - c

    return r




print(main())

