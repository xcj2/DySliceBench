#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))


def II(): return int(input())


def IF(): return float(input())


def S(): return input().rstrip()


def LS(): return S().split()


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
    def dfs(i):
        if c[i]:
            return
        for e in edg[i]:
            dfs(e)
        c[i] = 1
        top.append(i)
    n, m = LI()
    edg = [[] for i in range(n)]
    rev_edg = [[] for i in range(n)]
    for i in range(n + m - 1):
        a, b = LI_()
        edg[a].append(b)
        rev_edg[b].append(a)
    for i, e in enumerate(rev_edg):
        if len(e):
            continue
        root = i
        break
    c = defaultdict(int)
    top = []
    dfs(root)
    ind = [0] * n
    for i in range(n):
        ind[top[i]] = i
    ans = [-1] * n
    for i in range(n):
        tmp = [n, -1]
        for e in rev_edg[i]:
            if ind[e] < tmp[0]:
                tmp = [ind[e], e]
        ans[i] = tmp[1]
    print("\n".join(map(str, map(lambda x: x + 1, ans))))

    return


#main
if __name__ == '__main__':
    solve()
