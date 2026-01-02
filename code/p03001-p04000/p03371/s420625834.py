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
    A,B,C,x,y = LI()
    ans = float("inf")
    for c in range(0,2*(x+y+1),2):
        resa = max(0,x-(c >> 1))
        resb = max(0,y-(c >> 1))
        s = resa*A+resb*B+c*C
        if s < ans:
            ans = s
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
