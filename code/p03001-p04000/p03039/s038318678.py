import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)

def inv(x):
    return pow(x, mod - 2, mod)

# 1回だけの場合
def comb(n, b):
    if b > n - b:
        b = n - b
    r = 1
    for k in range(n, n-b, -1):
        r = r * k % mod
    d = 1
    for k in range(1, b+1):
        d = d * k % mod
    return r * inv(d) % mod

def main():
    n,m,k = LI()

    r = comb(n*m,k)
    cc = comb(n*m,2)
    tt = 0
    m2 = m * m
    n2 = n * n
    for i in range(n):
        v = (n-i) * (n-i-1) // 2
        tt += v * m2 % mod
        tt %= mod
    for i in range(m):
        v = (m-i) * (m-i-1) // 2
        tt += v * n2 % mod
        tt %= mod

    rr = r * k * (k-1) // 2 * tt
    rr = rr * inv(cc) % mod

    return rr%mod


print(main())

