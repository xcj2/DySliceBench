import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


fac = [-1] * (10**6+1)
finv = [-1] * (10**6+1)
inv = [-1] * (10**6+1)

fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

def initNCMMod(limit):
    for i in range(2, limit):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod
initNCMMod(10**5 + 3)
def NCMMod(n, k):
    if n < k:
        return 0
    if (n < 0 or k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

def main():
    N, K =LI()
    A = sorted(LI())
    m = A[0]
    if m < 0:
        for i in range(N):
            A[i] -= m
    arr = []
    cumA = [0] * (N+1)
    for i in range(N):
        A[i] %= mod
        cumA[i+1] = A[i] + cumA[i]
        cumA[i+1] %= mod
    ans = 0
    # [l, r) = A[l] + ... + A[r-1]
    if K >= 2:
        for d in range(K-2, N):
            ans += NCMMod(d, K-2) * (((cumA[N] - cumA[d+1]) % mod - (cumA[N-d-1] - cumA[0]) % mod)) % mod
            ans %= mod
    print(ans)

main()

