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
        n,m = LI()
        if n == 0 and m == 0:
            break
        a = sorted([LI()[::-1] for _ in range(n)], reverse=True)
        r = 0
        for i in range(n):
            ai = a[i]
            if ai[1] <= m:
                m -= ai[1]
                ai[1] = 0
            else:
                ai[1] -= m
                m = 0
            r += ai[0] * ai[1]
        rr.append(r)


    return '\n'.join(map(str, rr))


print(main())


