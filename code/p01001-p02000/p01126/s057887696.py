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
    rr = []

    while True:
        n,m,a = LI()
        if n == 0:
            break
        t = sorted([LI_() for _ in range(m)], reverse=True)
        r = list(range(n))
        for h,p,q in t:
            r[p],r[q] = r[q],r[p]

        rr.append(r.index(a-1)+1)

    return '\n'.join(map(str, rr))


print(main())


