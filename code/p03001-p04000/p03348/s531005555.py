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
    v = [[] for i in range(n)]
    d = [[float("inf")]*n for i in range(n)]
    f = [-1]*n
    for i in range(n):
        d[i][i] = 0
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        d[a][b] = 1
        d[b][a] = 1
        f[a] += 1
        f[b] += 1
        v[a].append(b)
        v[b].append(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                nd = d[i][k]+d[k][j]
                if nd < d[i][j]:
                    d[i][j] = nd

    for i in range(n):
        f[i] = max(f[i],1)
    x = 0
    for i in range(n):
        if d[0][x] < d[0][i]:
            x = i
    y = 0
    for i in range(n):
        if d[x][y] < d[x][i]:
            y = i
    k = (d[x][y]>>1)+1
    ans = float("inf")
    for s in range(n):
        if max(d[s]) < k:
            m = [0]*k
            m[0] = f[s]+1
            for i in range(n):
                fi = f[i]
                di = d[s][i]
                if m[di] < fi:
                    m[di] = fi
            na = 1
            for i in m:
                na *= i
            if na < ans:
                ans = na
        for t in v[s]:
            nd = [min(d[s][i],d[t][i]) for i in range(n)]
            if max(nd) < k:
                m = [0]*k
                m[0] = max(nd[s],nd[t])+1
                for i in range(n):
                    fi = f[i]
                    di = nd[i]
                    if m[di] < fi:
                        m[di] = fi
                na = 2
                for i in m:
                    na *= i
                if na < ans:
                    ans = na
    print(k,ans)
    return

#Solve
if __name__ == "__main__":
    solve()
