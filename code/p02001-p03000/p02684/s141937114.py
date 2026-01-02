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
    n,k = LI()
    a = LI()
    for i in range(n):
        a[i] -= 1
    p = [[a[i]] for i in range(n)]
    for i in range(60):
        for x in range(n):
            p[x].append(p[p[x][i]][i])
    x = 0
    while k:
        i = int(math.log(k,2))
        x = p[x][i]
        k -= 1<<i
    print(x+1)
    return

#Solve
if __name__ == "__main__":
    solve()
