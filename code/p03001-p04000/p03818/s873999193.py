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
    n = I()
    a = LI()
    c = defaultdict(lambda :0)
    for i in a:
        c[i] += 1
    a = [[i,2-(j&1)] for (i,j) in c.items()]
    a.sort()
    s = 0
    c = 0
    for i in range(len(a)):
        if a[i][1] == 2:
            c += 1
        s += a[i][1]
    s -= c
    if c&1:
        s -= 1
    print(s)
    return

#Solve
if __name__ == "__main__":
    solve()
