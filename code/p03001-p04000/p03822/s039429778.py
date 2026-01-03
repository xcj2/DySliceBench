# -*- coding: utf-8 -*-

import sys
from collections import Counter
from operator import itemgetter

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

def get_sum(a, b, c):
    """ 等差数列の和：(初項a, 末項b, 項数c) """
    return (a+b) * c // 2

def dfs(N, nodes, src):
    """ DFS(木、再帰、重みなし) """

    def rec(u, prev):
        C = Counter()
        for v in nodes[u]:
            if v != prev:
                C[rec(v, u) + 1] += 1
        if not C:
            return 0
        C = sorted(C.items(), key=itemgetter(0), reverse=1)
        mx = C[0][0]
        add = C[0][1] - 1
        vacant = 0
        for i, (k, v) in enumerate(C[1:], 1):
            k2, _ = C[i-1]
            vacant += k2 - k - 1
            vacant -= v - 1
            if vacant < 0:
                add += abs(vacant)
                vacant = 0
        return mx + add

    return rec(src, -1)

N = INT()
nodes = [[] for i in range(N)]
for a in range(1, N):
    b = INT()
    b -= 1
    nodes[a].append(b)
    nodes[b].append(a)

print(dfs(N, nodes, 0))
