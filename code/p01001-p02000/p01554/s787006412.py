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
def S(): return list(sys.stdin.readline())[:-1]
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
    d = defaultdict(lambda : 0)
    n = I()
    for i in range(n):
        u = input()
        d[u] = 1
    ans = ["Opened by", "Closed by"]
    m = I()
    k = 0
    for i in range(m):
        t = input()
        if not d[t]:
            print("Unknown",t)
        else:
            print(ans[k],t)
            k ^= 1
    return

#Solve
if __name__ == "__main__":
    solve()

