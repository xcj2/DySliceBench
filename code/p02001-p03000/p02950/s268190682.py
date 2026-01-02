#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
mod = 1000000007

def solve():
    def lagrange_interpolation(x,y,mod=mod):
        n = len(x)-1
        dp = [0]*(n+2)
        dp[0] = x[0]
        dp[1] = 1
        for i in range(n):
            nd = [0]*(n+2)
            ni = i+1
            for j in range(n+2):
                nj = j
                nd[nj] += -x[ni]*dp[j]
                nd[nj] %= mod
                if j <= n:
                    nj = j+1
                    nd[nj] += dp[j]
                    nd[nj] %= mod
            for j in range(n+2):
                dp[j] = nd[j]

        f = [0]*(n+1)
        for i in range(n+1):
            if y[i] == 0:
                continue
            fi = 1
            for j in range(n+1):
                if i == j:
                    continue
                fi *= x[i]-x[j]
                fi %= mod
            fi = pow(fi,mod-2,mod)
            p = [0]*(n+1)
            if x[i] == 0:
                for j in range(n+1):
                    p[j] = dp[j+1]
            else:
                inv = pow(x[i],mod-2,mod)
                p[0] = -dp[0]*inv%mod
                for j in range(1,n+1):
                    p[j] = (p[j-1]-dp[j])*inv%mod
            for j in range(n+1):
                f[j] += y[i]*fi*p[j]
                f[j] %= mod
        return f
    p = I()
    a = LI()
    f = lagrange_interpolation(list(range(p)),a,p)
    print(*f)
    return

#Solve
if __name__ == "__main__":
    solve()
