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
    def dfs(x):
        if r[x] != None:
            return 1
        f = 1
        res = 0
        for y in v[x]:
            if d[y]:
                d[y] = 0
                f &= dfs(y)
                d[y] = 1
            else:
                res = float("inf")
                f = 0
                break
            if res < r[y]:
                res = r[y]
        r[x] = res+1
        return f

    n = I()
    a = LIR(n)
    N = n*(n-1)
    f = [0]*N
    v = [[] for i in range(N)]
    lis = set()
    for i in range(n):
        for j in range(n-1):
            a[i][j] -= 1
        k = a[i][0]
        x = n*min(i,k)+max(i,k)
        for j in range(1,n-1):
            l = a[i][j]
            y = n*min(i,l)+max(i,l)
            v[y].append(x)
            f[x] += 1
            lis.add(x)
            lis.add(y)
            x = y
    if min([f[i] for i in lis]):
        print(-1)
        return
    d = [1]*N
    r = defaultdict(lambda : None)
    for i in lis:
        if not f[i]:
            d[i] = 0
            if not dfs(i):
                print(-1)
                return
    print(max(r.values()))
    return

#Solve
if __name__ == "__main__":
    solve()
