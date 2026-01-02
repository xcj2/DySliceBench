from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


class LCA(object):
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def get(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.logn):  # depthの差分だけuを遡らせる
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        if u == v: return u  # 高さ揃えた時点で一致してたら終わり

        for i in range(self.logn - 1, -1, -1):  # そうでなければ上から二分探索
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]

# query先読みで、頂点ごとに、どの色の長さを求めるのか。
n, q = LI()
edge_dict = [{} for _ in range(n)]
for u, v, c, d in LIR(n - 1):
    edge_dict[u - 1][v - 1] = (c, d)
    edge_dict[v - 1][u - 1] = (c, d)

lca = LCA(edge_dict)
query = [[] for _ in range(n)]
for q_idx, (x, y, u, v) in enumerate(LIR(q)):
    query[u - 1] += [(q_idx, x, y, 1)]
    query[v - 1] += [(q_idx, x, y, 1)]
    query[lca.get(u - 1, v - 1)] += [(q_idx, x, y, 0)]

def eulertour(G, root=0):
    n = len(G)
    euler = []
    depth = [-1] * n
    depth[root] = 0
    que = deque([root])
    que2 = deque()
    visited = [0] * n
    while que:
        u = que.pop()
        euler += [(depth[u], u)]
        if visited[u]:
            continue
        for v in G[u]:
            if visited[v]:
                que += [v]
            else:
                depth[v] = depth[u] + 1
                que2 += [v]
        que.extend(que2)
        que2 = deque()
        visited[u] = 1
    return euler

dist = 0
color_len = [0] * n
color_cnt = [0] * n
ans = [0] * q
euler = eulertour(edge_dict)
for i in range(1, len(euler)):
    dep = euler[i][0]
    c, d = edge_dict[euler[i - 1][1]][euler[i][1]]
    if euler[i - 1][0] < euler[i][0]:
        dist += d
        color_len[c] += d
        color_cnt[c] += 1
        for q_idx, x, y, flag in query[euler[i][1]]:
            if flag:
                ans[q_idx] += dist - color_len[x] + color_cnt[x] * y
            else:
                ans[q_idx] -= (dist - color_len[x] + color_cnt[x] * y) * 2
    else:
        dist -= d
        color_len[c] -= d
        color_cnt[c] -= 1


print(*ans, sep='\n')
