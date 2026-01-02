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
    def v(n):
        return [n*10%k, (n+1)%k]
    k = I()
    d = [float("inf")]*k
    d[1] = 1
    q = deque([1])
    while q:
        x = q.popleft()
        vx = v(x)
        dx = d[x]
        for c in range(2):
            nd = dx+c
            y = vx[c]
            if nd < d[y]:
                d[y] = nd
                if c:
                    q.append(y)
                else:
                    q.appendleft(y)
    print(d[0])
    return

#Solve
if __name__ == "__main__":
    solve()
