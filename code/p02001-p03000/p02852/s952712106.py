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
inf = float('INF')

import time
def Dijkstra(num, start, s, m):
    b = time.time()
    dist = [inf for i in range(num)]
    x = 0
    dist[0] = 0
    for i in range(num):
        if x > i:
            continue
        a = dist[i]
        for k in range(1, m + 1):
            if s[i + k] == "1":
                continue
            dist[i + k] = a + 1
            x = i + k
            if i + k == num - 1:
                return dist
        if x == i:
            x = inf
    return dist


#solve
def solve():
    n, m = LI()
    s = S()
    d = Dijkstra(n + 1, 0, s, m)
    if d[-1] == inf:
        print(-1)
        return
    ans = []
    q = deque([n])
    while q:
        a = q.pop()
        x = d[a]
        for i in range(min(a, m), 0, -1):
            if x - 1 == d[a - i]:
                q.append(a - i)
                ans.append(i)
                break
    ans = ans[::-1]
    print(" ".join(map(str, ans)))
    return


#main
if __name__ == '__main__':
    solve()
