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
    l = [1]
    p = [1]
    for i in range(n):
        l.append(l[-1]*2+3)
        p.append(p[-1]*2+1)

    def f(n,x):
        if x <= 0:
            return 0
        if n == 0:
            return 1
        nl = l[n]
        if x <= nl // 2:
            return f(n-1,x-1)
        r = p[n-1] + 1
        r += f(n-1, x - nl // 2 - 1)
        return r

    return f(n,x)


print(main())
