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
    def dfs(x,f):
        dx = d[x]
        for y,c in v[x]:
            if not f[y]:
                nd = dx+c
                if d[y] < nd:
                    d[y] = nd
                    f[y] = 1
                    dfs(y,f)
                    f[y] = 0
            else:
                nd = dx+c
                if nd > d[y]:
                    d[y] = float("inf")
                    dfs(y,f)
    n,m,p = LI()
    v = [[] for i in range(n)]
    for _ in range(m):
        a,b,c = LI()
        a -= 1
        b -= 1
        w = c-p
        v[a].append((b,w))
    d = [-float("inf")]*n
    d[0] = 0
    f = [0]*n
    f[0] = 1
    dfs(0,f)
    ans = d[n-1]
    if ans == float("inf") or ans == -float("inf"):
        print(-1)
    else:
        print(max(0,ans))
    return

#Solve
if __name__ == "__main__":
    solve()
