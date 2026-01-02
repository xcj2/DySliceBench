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
    n = I()
    p = LI()
    a = [0]*(n+1)
    a[p[0]] += 1
    a[p[1]] += 1
    a[p[2]] += 1
    ans = 0
    if sum(a[:p[1]]) == 1:
        ans += 1
    for i in range(2,n-1):
        a[p[i-2]] -= 1
        a[p[i+1]] += 1
        if sum(a[:p[i]]) == 1:
            ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
