#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    # 0-index
    edges.append([u-1, v-1])

# ある辺に着目したとき、それ以外の辺を一つずつグラフに追加し parents を更新する
# u <-> v を繋ぐ辺をグラフに追加した際、parents の u or v の親を更新する
# 全ての辺を繋ぎ終えたときの異なる親を数え、その値が 1 より多きければ着目したその辺は橋である


def root(u):
    if parents[u] < 0:
        return u
    parents[u] = root(parents[u])
    return parents[u]


def has_same_root(u, v):
    return root(u) == root(v)


def size(root_u):
    return -parents[root_u]


def unite(u, v):
    if has_same_root(u, v):
        return
    root_u = root(u)
    root_v = root(v)
    if size(root_u) > size(root_v):
        root_u, root_v = root_v, root_u
    parents[root_v] = root_u


ans = 0
for e_i in edges:
    parents = [-1 for _ in range(N)]
    for e_j in edges:
        if e_i == e_j:
            continue
        u, v = e_j
        unite(u, v)

    count = 0
    for i in range(N):
        if parents[i] < 0:
            count += 1
    if count > 1:
        ans += 1

print(ans)
