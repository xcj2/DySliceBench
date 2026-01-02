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
    def dp(a,b,s):
        if mem[(a,b,s)] is not None:
            return mem[(a,b,s)]
        x = a&1
        y = b&1
        z = s&1
        if x^y != z:
            return float("inf")
        res = 2*dp(a>>1,b>>1,s>>1)
        if a > 1:
            nr = 2*dp((a-1)>>1,(b+1)>>1,s>>1)+1
            if nr < res:
                res = nr
        mem[(a,b,s)] = res
        return res
    n = I()
    a = LI()
    s = 0
    for i in a[2:]:
        s ^= i
    b = a[1]
    a = a[0]
    mem = defaultdict(lambda : None)
    mem[(0,0,0)] = 0
    ans = dp(a,b,s)
    if ans == float("inf"):
        ans = -1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
