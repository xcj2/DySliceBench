#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
mod = 1000000007

def solve():
    def comb(a,b):
        return f[a]*inv[b]*inv[a-b]%mod
    r1,c1,r2,c2 = LI()
    N = 3*10**6
    f = [1]
    for i in range(N):
        f.append(f[-1]*(i+1)%mod)
    inv = [None]*(N+1)
    inv[-1] = pow(f[-1],mod-2,mod)
    for i in range(N)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod
    ans = 0
    for i in range(r1,r2+1):
        s = 0
        ans += comb(i+1+c2,i+1)-comb(i+c1,i+1)
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
