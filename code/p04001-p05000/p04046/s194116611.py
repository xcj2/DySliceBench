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
    f = [1]
    N = 1000000
    for i in range(1,N+1):
        f.append(f[-1]*i%mod)
    inv = [None]*(N+1)
    inv[N] = pow(f[N],mod-2,mod)
    for i in range(N)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod
    def comb(a,b):
        return f[a]*inv[b]*inv[a-b]%mod
    h,w,a,b = LI()
    ans = 0
    y = h-a
    x = b+1
    while x <= w and y:
        ans += comb(x+y-2,x-1)*comb(h-y+w-x,w-x)%mod
        y -= 1
        x += 1
    print(ans%mod)
    return

#Solve
if __name__ == "__main__":
    solve()
