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
    a,b,c,d = LI()
    ans = max(a*c,a*d,b*c,b*d)
    if ans < 0:
        if a <= 0 and 0 <= b:
            ans = 0
        if c <= 0 and 0 <= d:
            ans = 0
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
