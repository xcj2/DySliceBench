#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    x, a, b = LI()
    if b <= a:
        print("delicious")
    elif b <= a + x:
        print("safe")
    else:
        print("dangerous")

    return

#B
def B():
    n = II()
    a = IR(n)
    check = [False] * (n + 1)
    check[1] = True
    now = a[0]
    for i in range(1,n+1):
        if check[now]:
            break
        if now == 2:
            print(i)
            return
        check[now] = True
        now = a[now - 1]
    print(-1)
    return

#C
def C():
    return

#D
def D():
    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y: return False
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    n = II()
    par = [i for i in range(n)]
    rank = [0] * n
    xy = LIR(n)
    for i in range(n):
        xy[i].append(i)
    xy.sort(key=lambda x: x[0])
    edg = [None] * (2 * n - 2)
    a = 0
    for i in range(n-1):
        edg[i] = [xy[i + 1][0] - xy[i][0], xy[i][2], xy[i + 1][2]]
    xy.sort(key=lambda x: x[1])
    for i in range(n-1):
        edg[n + i - 1] = [xy[i + 1][1] - xy[i][1], xy[i][2], xy[i + 1][2]]
    ans = 0
    a = 0
    edg.sort(key=lambda x: x[0])
    for i in range(2 * n - 2):
        value, p0, p1 = edg[i]
        if a == n - 1:
            break
        if unite(p0, p1):
            a += 1
            ans += value
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
