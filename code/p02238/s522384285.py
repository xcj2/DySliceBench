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

cnt = 1
def solve():
    global cnt
    def dfs(x):
        global cnt
        f[x] = cnt
        for y in v[x]:
            if not d[y]:
                d[y] = cnt
                cnt += 1
                dfs(y)
        f[x] = cnt
        cnt += 1

    n = I()
    v = []
    for i in range(n):
        e = LI()
        u = e[2:]
        for i in range(len(u)):
            u[i] -= 1
        v.append(u)
    d = [0]*n
    f = [0]*n
    for i in range(n):
        if not d[i]:
            d[i] = cnt
            cnt += 1
            dfs(i)
    for i in range(n):
        print(i+1,d[i],f[i])
    return

#Solve
if __name__ == "__main__":
    solve()

