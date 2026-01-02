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
    n = I()
    p = [input().split() for _ in range(n)]
    dr = defaultdict(lambda : [])
    dl = defaultdict(lambda : [])
    du = defaultdict(lambda : [])
    dd = defaultdict(lambda : [])
    ans = float("inf")
    for i in range(n):
        p[i][0] = int(p[i][0])
        p[i][1] = int(p[i][1])
        x,y,d = p[i]
        if d == "L":
            dl[y].append(x)
        elif d == "R":
            dr[y].append(x)
        elif d == "U":
            du[x].append(y)
        else:
            dd[x].append(y)
    for x in dl.keys():
        dl[x].sort()
    for x in dr.keys():
        dr[x].sort()
    for x in du.keys():
        du[x].sort()
    for x in dd.keys():
        dd[x].sort()
    for x,y,d in p:
        if d == "L":
            if dr[y]:
                i = bisect.bisect_left(dr[y],x)-1
                if i >= 0:
                    s = x-dr[y][i]
                    if s < ans:
                        ans = s
        elif d == "R":
            if dl[y]:
                i = bisect.bisect_right(dl[y],x)
                if i < len(dl[y]):
                    s = dl[y][i]-x
                    if s < ans:
                        ans = s
        elif d == "D":
            if du[x]:
                i = bisect.bisect_left(du[x],y)-1
                if i >= 0:
                    s = y-du[x][i]
                    if s < ans:
                        ans = s
        else:
            if dd[x]:
                i = bisect.bisect_right(dd[x],y)
                if i < len(dd[x]):
                    s = dd[x][i]-y
                    if s < ans:
                        ans = s
    dux = defaultdict(lambda : [])
    ddx = defaultdict(lambda : [])
    duy = defaultdict(lambda : [])
    ddy = defaultdict(lambda : [])
    for i,(a,b,d) in enumerate(p):
        x = a-b
        y = a+b
        p[i][0] = x
        p[i][1] = y
        if d == "U":
            dux[y].append(x)
            duy[x].append(y)
        elif d == "D":
            ddx[y].append(x)
            ddy[x].append(y)
    for x in dux.keys():
        dux[x].sort()
    for x in ddx.keys():
        ddx[x].sort()
    for x in duy.keys():
        duy[x].sort()
    for x in ddy.keys():
        ddy[x].sort()
    for x,y,d in p:
        if d == "L":
            if ddx[y]:
                i = bisect.bisect_left(ddx[y],x)-1
                if i >= 0:
                    s = x-ddx[y][i]
                    if s < ans:
                        ans = s
            if duy[x]:
                i = bisect.bisect_left(duy[x],y)-1
                if i >= 0:
                    s = y-duy[x][i]
                    if s < ans:
                        ans = s
        elif d == "R":
            if dux[y]:
                i = bisect.bisect_right(dux[y],x)
                if i < len(dux[y]):
                    s = dux[y][i]-x
                    if s < ans:
                        ans = s
            if ddy[x]:
                i = bisect.bisect_right(ddy[x],y)
                if i < len(ddy[x]):
                    s = ddy[x][i]-y
                    if s < ans:
                        ans = s
    if ans == float("inf"):
        print("SAFE")
    else:
        print(ans*5)
    return

#Solve
if __name__ == "__main__":
    solve()
