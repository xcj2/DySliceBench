#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')

n_nodes, m_edges = map(int, input().split())
edges = []
for _ in range(m_edges):
    u, v = map(int, input().split())
    edges.append([u - 1, v - 1])
# pprint(edges)


def find_root(v):
    if v != parents[v]:
        parents[v] = find_root(parents[v])
    return parents[v]


def has_same_root(u, v):
    return find_root(u) == find_root(v)


def unite(u, v):
    root_u, root_v = find_root(u), find_root(v)
    if root_u == root_v:
        return
    if rank[root_u] < rank[root_v]:
        root_u, root_v = root_v, root_u
    parents[root_v] = root_u
    rank[root_u] += rank[root_v]


res = 0
for i in range(m_edges):
    parents = [i for i in range(n_nodes)]
    rank = [1] * n_nodes
    for j in range(m_edges):
        if i == j:
            continue
        u, v = edges[j]
        if not has_same_root(u, v):
            unite(u, v)
    # pprint(parents)
    count = 0
    for v in range(n_nodes):
        if parents[v] == v:
            count += 1
    if count > 1:
        res += 1

print(res)
