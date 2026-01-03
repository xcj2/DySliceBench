#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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
    n,a = LI()
    x = LI()
    m = 2501
    d = [[0]*m for i in range(n+1)]
    d[0][0] = 1
    for xi in x:
        for i in range(n)[::-1]:
            ni = i+1
            for j in range(m):
                if not d[i][j]:
                    continue
                k = j+xi
                if k >= m:
                    break
                d[ni][k] += d[i][j]
    ans = 0
    for i in range(1,n+1):
        k = a*i
        if k < m:
            ans += d[i][k]
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
