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
    n = I()
    a = LI()
    N = 10**6
    f = [1]*(N+1)
    a.sort()
    cnt = [0]*(N+1)
    for i in a:
        cnt[i] += 1
    for i in range(N+1):
        if cnt[i] > 1:
            f[i] = 0
            x = i
            while x <= N:
                f[x] = 0
                x += i
    ans = 0
    for i in a:
        if f[i]:
            ans += 1
            x = i
            while x <= N:
                f[x] = 0
                x += i
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
