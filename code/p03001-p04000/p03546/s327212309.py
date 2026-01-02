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
    h,w = LI()
    d = LIR(10)
    for k in range(10):
        for i in range(10):
            for j in range(10):
                nd = d[i][k]+d[k][j]
                if nd < d[i][j]:
                    d[i][j] = nd
    a = LIR(h)
    ans = 0
    for i in a:
        for j in i:
            if j < 0:
                continue
            ans += d[j][1]
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
