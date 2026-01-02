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
    n,m,q = LI()
    a = [[0]*n for i in range(n)]
    for _ in range(m):
        l,r = LI()
        l -= 1
        r -= 1
        a[l][r] += 1
    for i in range(n):
        for j in range(n-1):
            a[i][j+1] += a[i][j]
    for j in range(n):
        for i in range(n-1)[::-1]:
            a[i][j] += a[i+1][j]
    for _ in range(q):
        l,r = LI()
        l -= 1
        r -= 1
        print(a[l][r])
    return

#Solve
if __name__ == "__main__":
    solve()
