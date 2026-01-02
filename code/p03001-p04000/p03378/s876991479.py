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
    n,m,x = LI()
    t = LI()
    a = collections.defaultdict(int)
    for c in t:
        a[c] = 1
    r = inf
    tr = 0
    for i in range(x+1,n):
        tr += a[i]
    r = tr
    tr = 0
    for i in range(x-1,-1,-1):
        tr += a[i]
    if r > tr:
         r = tr

    return r


print(main())


