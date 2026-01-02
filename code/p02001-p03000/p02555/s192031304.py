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
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    def comb(a,b):
        if a < b:
            return 0
        return f[a]*inv[b]*inv[a-b]
    s = I()
    N = 1000000
    f = [1]*(N+1)
    for i in range(N):
        f[i+1] = f[i]*(i+1)%mod
    inv = [None]*(N+1)
    inv[N] = pow(f[N],mod-2,mod)
    for i in range(N)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod
    ans = 0
    for i in range(1,s//3+1):
        n = s-3*i
        ans += comb(n+i-1,n)
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
