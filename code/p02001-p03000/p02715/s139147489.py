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
    n,k = LI()
    f = [1]*(k+1)
    p = 2
    phi = list(range(k+1))
    while p <= k:
        while p <= k and not f[p]:
            p += 1
        j = p
        x = (p-1)*pow(p,mod-2,mod)%mod
        while j <= k:
            phi[j] *= x
            phi[j] %= mod
            f[j] = 0
            j += p
        p += 1
    ans = 0
    for i in range(1,k+1):
        ans += phi[i]*pow(k//i,n,mod)
    print(ans%mod)
    return

#Solve
if __name__ == "__main__":
    solve()
