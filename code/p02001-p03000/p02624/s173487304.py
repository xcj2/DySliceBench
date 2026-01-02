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
mod = 1000000007

def solve():
    N = I()
    f = [1]*(N+1)
    for p in range(2,N+1):
        f[p] += 1
        j = 2*p
        fp = f[p]
        while j <= N:
            f[j] += 1
            j += p
    ans = 0
    for i in range(1,N+1):
        ans += i*f[i]
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
