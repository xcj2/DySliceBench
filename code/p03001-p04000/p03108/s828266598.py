#!/usr/bin/env python3

from pprint import pprint
import sys

sys.setrecursionlimit(10 ** 6)


# 辺を取り除くのではなく、辺が無い状態から始めて辺を順にグラフに追加していくことを考える
# 最初は辺が無いので不便さは N * (N-1) / 2
# 辺 u <-> v を追加したとき、頂点 u, v が既に到達可能であるなら、不便さは変わらない
# そうでなければ、不便さは直前の値より size[u] * size[v] だけ小さくなる

N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    # 0-index
    edges.append([u-1, v-1])


def root(v):
    if parents[v] < 0:
        return v
    parents[v] = root(parents[v])
    return parents[v]


def has_same_root(u, v):
    return root(u) == root(v)


# unite by size
def unite(u, v):
    u_root = root(u)
    v_root = root(v)
    if size(u_root) > size(v_root):
        u_root, v_root = v_root, u_root
    parents[u_root] -= size(v_root)
    parents[v_root] = u_root


def size(v):
    return -parents[root(v)]


# the parent node of a root node has the size of tree (negative value)
parents = [-1 for v in range(N)]

ans = []
current = N * (N-1) // 2
for i in range(M):
    u, v = edges[M-1-i]
    # print(f'current = {current}')
    # print(f'u = {u}, v = {v}')
    # print(f'parents = {parents}')
    ans.append(current)
    if has_same_root(u, v):
        # print('skip')
        continue
    # print(f'size(u) = {size(u)}, size(v) = {size(v)}')
    current -= size(u) * size(v)
    unite(u, v)
    # print(f'parents = {parents}\n')

for i in reversed(range(M)):
    print(ans[i])
