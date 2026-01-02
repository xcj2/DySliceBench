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
    n,m = LI()
    d = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]
    for _ in range(m):
        a,b,c = LI()
        d[a][b] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                nd = d[i][k]+d[k][j]
                if nd < d[i][j]:
                    d[i][j] = nd
    for i in range(n):
        if d[i][i] < 0:
            print("NEGATIVE CYCLE")
            return
        for j in range(n):
            if d[i][j] == float("inf"):
                d[i][j] = "INF"
    for i in d:
        print(*i,sep = " ")
    return

#Solve
if __name__ == "__main__":
    solve()

