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
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    
    def same(x,y):
        return root(x) == root(y)
    
    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    n = II()
    v = LIR(n)
    l = [None for i in range(2*n-2)]
    for i in range(n):
        v[i].append(i)
    par = [i for i in range(n)]
    rank = [0 for i in range(n)]
    v.sort(key = lambda x:x[0])
    for i in range(n-1):
        l[i] = [v[i][2],v[i+1][2],v[i+1][0]-v[i][0]]
    v.sort(key = lambda x:x[1])
    for i in range(n-1):
        l[i+n-1] = [v[i][2],v[i+1][2],v[i+1][1]-v[i][1]]
    l.sort(key = lambda x:x[2])
    k = 0
    ans = 0
    for i in range(2*n-2):
        x,y,c = l[i]
        if not same(x,y):
            k += 1
            ans += c
            unite(x,y)
        if k == n-1:break
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
