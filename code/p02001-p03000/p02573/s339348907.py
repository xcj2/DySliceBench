# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

class UnionFind(object):
    def __init__(self, n: int):
        """ ノードのつながりを辞書型で表現する
        要素数nであり、要素は0からn-1である想定
        >> - usage
        g = Graph(n=n)

        """
        self.adjacency_dict = {}
        self.parent = [None] * n

        for i in range(n):
            self.add_vertex(i)
            self.parent[i] = i
        self.rank = [0] * n

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = []

    def unite(self, v1: int, v2: int):
        """ ノード同士をつなぐ。"""
        if v1 == v2:
            return

        # すでにつながっている場合は親の更新のみしておく
        if self.same(v1, v2):
            return

        p1 = self.parent[v1]
        p2 = self.parent[v2]

        # つながっていない場合は親同士をつなげる
        # その場合rankが小さい方から大きい方につなげる
        if self.rank[p1] == self.rank[p2]:
            self.update(p1, p2)
            self.rank[p2] += 1
        elif self.rank[p1] < self.rank[p2]:
            self.update(p1, p2)
        else:
            self.update(p2, p1)

    def update(self, v, parent):
        self.adjacency_dict[v].append(parent)

    def same(self, v1, v2):
        """ 親が同一であれば連結 """
        self.parent[v1] = self.root(v1)
        self.parent[v2] = self.root(v2)

        return self.parent[v1] == self.parent[v2]

    def root(self, v1):
        """ vから上向きに辿って根を調べる """
        if self.adjacency_dict[v1] == []:
            return v1

        for v in self.adjacency_dict[v1]:
            parent = self.root(v)
        return parent

    def print_graph(self):
        print(self.adjacency_dict)


u = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    u.unite(a, b)

dic = defaultdict(int)
ans = 0
for i in range(N):
    val = u.root(i)
    # print(i, val)
    dic[val] += 1
    ans = max(ans, dic[val])

print(ans)
