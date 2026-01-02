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

# どの島も繋がっていないとき、不便さは最大値 N * (N-1) / 2 を取る
# 1 本ずつ減らすのではなく、最悪のケースから順に辺を追加していくことを考える
# ある辺 u <-> v を追加したときに、島の集合 a と島の集合 b が連結になったとすると、
# 不便さは size(a) * size(b) だけ減る
# disjoint set として島を管理し、最悪のケースから各辺を追加したときの不便さを計算すればよい


def has_same_root(u, v):
    return root(u) == root(v)


def root(u):
    if parents[u] < 0:
        return u
    parents[u] = root(parents[u])
    return parents[u]


def unite(u, v):
    # print(f'unite {u}, {v}')
    u_root = root(u)
    v_root = root(v)
    # pprint(parents)
    # print(f'u_root = {u_root}, v_root = {v_root}')
    # print(f'size(u_root) = {size(u_root)}, size(v_root) = {size(v_root)}')
    if size(u_root) > size(v_root):
        u_root, v_root = v_root, u_root
    parents[u_root] -= size(v_root)
    parents[v_root] = u_root
    # pprint(parents)


def size(u):
    return -parents[root(u)]


parents = [-1 for _ in range(N)]
inconvenience = N * (N-1) // 2
ans = [inconvenience]

for u, v in reversed(edges):
    # print(f'\nu = {u}, v = {v}')
    if not has_same_root(u, v):
        inconvenience -= size(u) * size(v)
        unite(u, v)
    ans.append(inconvenience)

for i in reversed(range(M)):
    print(ans[i])
