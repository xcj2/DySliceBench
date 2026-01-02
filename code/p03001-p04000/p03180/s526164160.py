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
    n = I()
    a = [LI() for _ in range(n)]
    m = 2**n

    b = [None] * m
    b[0] = 0
    ii = [2**i for i in range(n+1)]
    dd = {}
    for i in range(n):
        dd[ii[i]] = i
    c = 0
    for i in range(1,m):
        if i >= ii[c+1]:
            c += 1
        t = i - ii[c]
        k = b[t]
        d = a[c]
        while t:
            u = t ^ t - 1 & t
            t ^= u
            k += d[dd[u]]
        b[i] = k

    d = b[:]
    c = 0
    for i in range(1,m):
        if i >= ii[c+1]:
            c += 1
        k = d[i - ii[c]]
        t = i
        while t:
            u = d[t] + d[i^t]
            if k < u:
                k = u
            t = t-1 & i
        d[i] = k

    # print('b',b)
    # print('d',d)

    return d[-1]



print(main())

