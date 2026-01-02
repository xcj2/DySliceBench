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
    n,k = LI()
    a = LI()
    bi = bisect.bisect_left(a, 0)
    r = inf
    if bi >= k:
        r = abs(a[bi-k])
    if bi+k-1 < n and r > a[bi+k-1]:
        r = a[bi+k-1]
    for i in range(1, n):
        if 0 > bi - i or bi + k - i - 1 >= n or bi + k - i - 1 < bi:
            continue
        t = -a[bi-i]
        u = a[bi+k-i-1]
        s = t + u + min(t,u)
        if r > s:
            r = s
    return r



print(main())
