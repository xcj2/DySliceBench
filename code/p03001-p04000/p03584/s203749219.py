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

def pf(s):
    print(s, flush=True)

def main():
    n,k = LI()
    t = [LI() for _ in range(n)]

    d = {}
    d[k] = 0
    j = 0
    for i in range(30,-1,-1):
        ii = 2**i
        if k & ii > 0:
            d[j+ii-1] = 0
            j += ii
    js = d.keys()
    for a,b in t:
        for j in js:
            if j & a ^ a == 0:
                d[j] += b
    return max(d.values())




print(main())




