#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)
INF = float('inf')


N, M = map(int, input().split())

edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append([u-1, v-1])
# pprint(edges)


# ある辺iを除いた残りの辺にそれぞれに対してuniteの操作を行ったのち、異なるparentsの数を数える
# 連結グラフであれば、異なるparentsの数は1になる
# 非連結グラフであれば、異なるparentsの数は2以上になる


def root(v):
    if parents[v] == v:
        return v
    parents[v] = root(parents[v])
    return parents[v]


def unite(u, v):
    u_root = root(u)
    v_root = root(v)
    if u_root == v_root:
        return
    parents[u_root] = v_root


def same(u, v):
    return root(u) == root(v)


ans = 0
for e_i in edges:
    parents = [i for i in range(N)]
    for e_j in edges:
        if e_i == e_j:
            continue
        u, v = e_j
        if not same(u, v):
            unite(u, v)
    count = 0
    for v in range(N):
        if parents[v] == v:
            count += 1
    if count > 1:
        ans += 1

print(ans)
