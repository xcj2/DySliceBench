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
    n,h = LI()
    a = []
    b = []
    for _ in range(n):
        c,d = LI()
        a.append(c)
        b.append(d)
    ma = max(a)
    b = sorted(b, reverse=True)
    r = 0
    for c in b:
        if c <= ma:
            break
        r+=1
        h-=c
        if h<=0:
            return r

    r += h//ma
    if h%ma!=0:
        r += 1
    return r

print(main())


