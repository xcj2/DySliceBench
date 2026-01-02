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
    n,s = LI()
    a = LI()
    ans = 0
    f = [0]*(s+1)
    f[0] = 0
    for i in a:
        f[0] += 1
        for j in range(s+1)[::-1]:
            nj = j+i
            if nj > s:
                continue
            f[nj] += f[j]
            f[nj] %= mod
        ans += f[s]
        ans %= mod
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
