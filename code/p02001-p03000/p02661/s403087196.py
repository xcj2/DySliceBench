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
    g = LIR(n)
    if n&1:
        g.sort()
        l = g[n>>1][0]
        g.sort(key = lambda x:x[1])
        r = g[n>>1][1]
        print(r-l+1)
    else:
        g.sort()
        l = g[(n>>1)-1][0]+g[(n>>1)][0]
        g.sort(key = lambda x:x[1])
        r = g[n>>1][1]+g[(n>>1)-1][1]
        print(r-l+1)
    # ans = set()
    # # for i in range(g[0][0],g[0][1]+1):
    # #     for j in range(g[1][0],g[1][1]+1):
    # #         for k in range(g[2][0],g[2][1]+1):
    # #             p = [i,j,k]
    # #             p.sort()
    # #             ans.add(p[1])
    # for i in range(g[0][0],g[0][1]+1):
    #     for j in range(g[1][0],g[1][1]+1):
    #         ans.add((i+j)/2)
    # ans = list(ans)
    # ans.sort()
    # print(len(ans))
    return

#Solve
if __name__ == "__main__":
    solve()
