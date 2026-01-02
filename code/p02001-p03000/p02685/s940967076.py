#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 998244353

def solve():
    def comb(n,k):
        return f[n]*inv[k]*inv[n-k]%mod
    n,m,k = LI()
    if k == 0:
        print(m*pow(m-1,n-1,mod)%mod)
    else:
        f = [1]
        N = 10**6
        for i in range(1,N+1):
            f.append(f[-1]*i%mod)
        inv = [None]*(N+1)
        inv[N] = pow(f[N],mod-2,mod)
        for i in range(N)[::-1]:
            inv[i] = inv[i+1]*(i+1)%mod
        s = m
        dk = m
        p = m-1
        for i in range(n-1):
            s *= m
            s %= mod
            if i >= k:
                s -= dk
                s %= mod
                dk *= m-1
                dk += comb(i,k-1)*m*p%mod
                dk %= mod
                p *= m-1
                p %= mod
        print(s)
    return

#Solve
if __name__ == "__main__":
    solve()
