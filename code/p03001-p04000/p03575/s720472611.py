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
cnt = 0
def solve():
    def lowlink(v):
        global cnt
        def dfs(x):
            global cnt
            for y in v[x]:
                if pre[y] is None:
                    cnt += 1
                    pre[y] = low[y] = cnt
                    par[y] = x
                    py = dfs(y)
                    if py < low[x]:
                        low[x] = py
                else:
                    if par[x] != y and pre[y] < low[x]:
                        low[x] = pre[y]
                if pre[x] < low[y]:
                    res.append((x,y))
            return low[x]

        pre = [None]*n
        low = [None]*n
        par = [None]*n
        res = []
        for x in range(n):
            if pre[x] is None:
                pre[x] = low[x] = cnt
                dfs(x)
        return res

    n,m = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    ans = lowlink(v)
    print(len(ans))
    return

#Solve
if __name__ == "__main__":
    solve()
