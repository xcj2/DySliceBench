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
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    n = I()
    p = LIR(n)
    for i in range(n):
        p[i].append(i)
    p.sort()
    v = []
    for i in range(n-1):
        x,y,c = p[i]
        a,b,d = p[i+1]
        v.append((min(abs(x-a),abs(y-b)),c,d))
    p.sort(key = lambda x:x[1])
    for i in range(n-1):
        x,y,c = p[i]
        a,b,d = p[i+1]
        v.append((min(abs(x-a),abs(y-b)),c,d))
    v.sort()
    par = [i for i in range(n)]
    rank = [0]*n
    ans = 0
    s = 1
    for c,a,b in v:
        if root(a) != root(b):
            ans += c
            s += 1
            if s >= n:
                break
            unite(a,b)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
