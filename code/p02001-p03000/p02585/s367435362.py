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
    p = LI()
    for i in range(n):
        p[i] -= 1
    c = LI()
    bfs = [0]*n
    lis = []
    for i in range(n):
        if not bfs[i]:
            bfs[i] = 1
            x = i
            path = [c[x]]
            while 1:
                x = p[x]
                if bfs[x]:
                    break
                path.append(c[x])
                bfs[x] = 1
            lis.append([0]+list(accumulate(path*2)))
    ans = -float("inf")
    for path in lis:
        n = len(path) >> 1
        m = k//n
        if k%n == 0:
            m -= 1
        s = m*path[n]
        if s < 0:
            s = 0
            res = n
        else:
            res = k-m*n
        for l in range(n):
            for j in range(1,res+1):
                ns = s+path[l+j]-path[l]
                if ans < ns:
                    ans = ns
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
