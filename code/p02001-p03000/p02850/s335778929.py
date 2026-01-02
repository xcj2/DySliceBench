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

#solve
def solve():
    n = II()
    ed = [[] for i in range(n)]
    edg = defaultdict(int)
    ans = [None] * (n - 1)
    for i in range(n - 1):
        a, b = LI_()
        ed[a].append((b, i))
        ed[b].append((a, i))
        edg[a] += 1
        edg[b] += 1
    ma = max(edg.values())
    print(ma)
    for num, a in enumerate(ed):
        if len(a) == ma:
            break
    q = deque([num])
    while q:
        a = q.pop()
        o = 1
        li = defaultdict(int)
        for b, i in ed[a]:
            if ans[i] != None:
                li[ans[i]] = 1
        for b, i in ed[a]:
            if ans[i] == None:
                q.appendleft(b)
                while li[o]:
                    o += 1
                ans[i] = o
                o += 1
    for i in ans:
        print(i)
    return


#main
if __name__ == '__main__':
    solve()
