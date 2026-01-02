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

#A
def A():
    a = II()
    s = input()
    print(s if a >= 3200 else "red")
    return

#B
def B():
    II()
    a = LI()
    ans = 0
    for ai in a:
        ans += 1 / ai
    print(1/ans)
    return

#C
def C():
    n = II()
    v = LI()
    q = []
    for vi in v:
        heappush(q, vi)
    while 1:
        a = heappop(q)
        if q:
            b = heappop(q)
            heappush(q, (a + b) / 2)
        else:
            print(a)
            return

#D
def D():
    n, q = LI()
    tree = [[] for i in range(n)]
    for _ in range(n - 1):
        a, b = LI_()
        tree[a].append(b)
        tree[b].append(a)
    ans = [0] * n
    c = defaultdict(int)
    def dfs(now):
        for nex in tree[now]:
            if c[nex]:
                continue
            c[nex] += 1
            ans[nex] += ans[now]
            dfs(nex)
    for _ in range(q):
        p, x = LI_()
        x += 1
        ans[p] += x
    c[0] = 1
    dfs(0)
    print(*ans)
    return

#E
def E():
    return

#F
def F():
    return

#Solve
if __name__ == '__main__':
    A()
