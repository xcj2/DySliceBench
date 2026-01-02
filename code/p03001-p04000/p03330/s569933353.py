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
    n,C = LI()
    d = LIR(C)
    c = LIR(n)
    ans = 0
    s = [[0]*C for i in range(3)]
    for i in range(n):
        for j in range(n):
            s[(i+j)%3][c[i][j]-1] += 1
    ans = float("inf")
    for x in range(C):
        bx = 1<<x
        for y in range(C):
            if x == y:
                continue
            by = 1<<y
            for z in range(C):
                if z == x or z == y:
                    continue
                cost = 0
                for j in range(C):
                    cost += s[0][j]*d[j][x]
                    cost += s[1][j]*d[j][y]
                    cost += s[2][j]*d[j][z]
                if cost < ans:
                    ans = cost
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
