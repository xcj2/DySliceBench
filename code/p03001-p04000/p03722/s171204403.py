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
    a, b, c = LI()
    if a <= c <= b:
        print("Yes")
        return
    print("No")
    return

#B
def B():
    n, m = LI()
    e = defaultdict(int)
    for i in range(1, n + 1): e[i] = 0
    for i in range(m):
        a, b = LI()
        e[a] += 1
        e[b] += 1
    for i in e.values():
        print(i)
    return

#C
def C():
    n, k = LI()
    d = defaultdict(int)
    for i in range(1, 10**5+1): d[i] = 0
    for i in range(n):
        a, b = LI()
        d[a] += b
    for key, valus in d.items():
        k -= valus
        if k <= 0:
            print(key)
            return
    return

#D
def D():
    n, m = LI()
    abc = LIR_(m)
    for i in range(m):
        abc[i][2] = -abc[i][2] - 1
    dist = [inf] * n
    dist[0] = 0
    for _ in range(n - 1):
        for a, b, c in abc:
            dist[b] = min(dist[a] + c , dist[b])
    check = [False] * n
    for _ in range(n):
        for a, b, c in abc:
            if check[a]:
                check[b] = True
            if dist[b] > dist[a] + c:
                check[b] = True
                dist[b] = dist[a] + c
    if check[n - 1]:
        print("inf")
    else:
        print(-dist[n - 1])
    return

#Solve
if __name__ == '__main__':
    D()
