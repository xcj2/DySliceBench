#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n, u, v = LI_()
    n += 1
    edg = [[] for i in range(n)]
    for _ in range(n-1):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    dist_u = [-1] * n
    dist_u[u] = 0
    dist_v = [-1] * n
    dist_v[v] = 0
    q = deque([u])
    while q:
        p = q.pop()
        dp = dist_u[p]
        for e in edg[p]:
            if dist_u[e] < 0:
                dist_u[e] = dp + 1
                q.append(e)
    q = deque([v])
    while q:
        p = q.pop()
        dp = dist_v[p]
        for e in edg[p]:
            if dist_v[e] < 0:
                dist_v[e] = dp + 1
                q.append(e)
    ans = 0
    while dist_u[v] - dist_u[u] > 2:
        for e in edg[u]:
            if dist_v[e] < dist_v[u]:
                u = e
                continue
        for e in edg[v]:
            if dist_u[v] > dist_u[e]:
                v = e
                continue
        ans += 1
    f = dist_u[v]-dist_u[u] == 2
    ans += f
    q = deque([u])
    dist_u = [-1] * n
    for e in edg[v]:
        dist_u[e] = 1
    dist_u[u] = 0
    while q:
        u = q.pop()
        dp = dist_u[u]
        for e in edg[u]:
            if dist_u[e] < 0 and v != e:
                dist_u[e] = dp + 1
                q.append(e)
    if f and max(dist_u) == 1:
        ans -= 1
    print(max(dist_u)+ ans)

    return


#main
if __name__ == '__main__':
    solve()
