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
    n,C = LI()
    a = [LI() for _ in range(n)]
    u = [_[0] for _ in a]
    x = [_[1] for _ in a]
    b = [0] * n
    c = [0] * n
    d = [0] * n
    e = [0] * n
    b[0] = x[0]
    c[-1] = x[-1]
    for i in range(1, n):
        b[i] = b[i-1] + x[i]
    for i in range(n-2, -1, -1):
        c[i] = c[i+1] + x[i]
    d[0] = x[0] - u[0]
    e[-1] = x[-1] - (C-u[-1])
    for i in range(1, n):
        d[i] = max(b[i]-u[i], d[i-1])
    for i in range(n-2, -1, -1):
        e[i] = max(c[i]-(C-u[i]), e[i+1])

    r = max(d[-1], e[0], 0)
    for i in range(n):
        if i < n-1 and r < b[i] - u[i] * 2 + e[i+1]:
            r = b[i] - u[i] * 2 + e[i+1]
        if i > 0 and r < c[i] - (C-u[i]) * 2 + d[i-1]:
            r = c[i] - (C-u[i]) * 2 + d[i-1]


    return r



print(main())

