import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def gcd(a,b):
    while b>0:
        a,b = b,a
        b %= a
    return a

def main():
    N,K = LI()
    a = LI()
    if max(a) < K:
        return 'IMPOSSIBLE'
    if K in a:
        return 'POSSIBLE'
    t = a[0]
    for c in a[1:]:
        t = gcd(c, t)
        if t <= 1:
            return 'POSSIBLE'
    for c in a:
        if (c > K) and (((c-K) % t) == 0):
            return 'POSSIBLE'

    return 'IMPOSSIBLE'


print(main())



