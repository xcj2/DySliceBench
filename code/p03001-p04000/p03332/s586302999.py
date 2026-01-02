import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def inv(x):
    return pow(x, mod - 2, mod)

nm = {}
nm[0] = 1
def nCr_(n):
    b = n // 2 + 1
    r = 1
    d = 1
    for k in range(1,b+1):
        r = r * (n-k+1) % mod
        d = d * k % mod
        nm[k] = r * inv(d) % mod

def nCr(n, b):
    if b > n - b:
        b = n - b
    return nm[b]

def main():
    n,a,b,k = LI()
    r = 0
    nCr_(n)
    for i in range(n+1):
        ai = a * i
        bi = k - ai
        if bi < 0 or bi % b > 0 or bi // b > n:
            continue
        bb = bi // b
        r += nCr(n,i) * nCr(n,bb)
        r %= mod

    return r


print(main())

