# -*- coding: utf-8 -*-
"""
C - 2D Plane 2N Points
https://beta.atcoder.jp/contests/abc091/tasks/arc092_a

"""
import sys
from sys import stdin
from collections import namedtuple, deque
input = stdin.readline


edge = namedtuple('edge', ['to', 'cap', 'rev'])

def add_edge(G, f, t, c):
    G[f].append(edge(t, c, len(G[t])))
    G[t].append(edge(f, 0, len(G[f]) - 1))


def bfs(G, level, s):
    for i in range(len(level)):
        level[i] = -1
    que = deque()
    level[s] = 0
    que.append(s)
    while que:
        v = que.popleft()
        for e in G[v]:
            if e.cap > 0 and level[e.to] < 0:
                level[e.to] = level[v] + 1
                que.append(e.to)


def dfs(G, iter, level, v, t, f):
    if v == t:
        return f
    for i in range(iter[v], len(G[v])):
        e = G[v][i]
        if e.cap > 0 and level[v] < level[e.to]:
            d = dfs(G, iter, level, e.to, t, min(f, e.cap))
            if d > 0:
                G[v][i] = edge(e.to, e.cap - d, e.rev)
                G[e.to][e.rev] = edge(G[e.to][e.rev].to, G[e.to][e.rev].cap + d, G[e.to][e.rev].rev)
                return d
    return 0


def max_flow(G, V, s, t):
    level = [0] * V
    flow = 0
    while True:
        bfs(G, level, s)
        if level[t] < 0:
            return flow
        iter = [0] * V
        while True:
            f = dfs(G, iter, level, s, t, float('inf'))
            if f > 0:
                flow += f
            else:
                break


def main(args):
    """
    - 追加したソースノードID: 0
    - 赤い点ID: 1〜N
    - 青い点ID: N+1 〜2N
    - 追加したシンクノードID: 2N + 1(2N + 2 - 1)
    として、ノード0 → 2N+1 への最大流を求める
    """
    N = int(input())
    G = [[] for _ in range(N*2 + 2)]
    red_points = []
    for ri in range(1, N+1):
        rx, ry = map(int, input().split())
        red_points.append([rx, ry])
        add_edge(G, 0, ri, 1)   #  ソースノードは全ての赤い点と繋ぐ

    for bi in range(1, N+1):
        bx, by = map(int, input().split())
        add_edge(G, bi+N, N*2+1, 1) #  全ての青い点はシンクノードに繋ぐ
        for i, r in enumerate(red_points, start=1):
            rx = r[0]
            ry = r[1]
            if rx < bx and ry < by:
                add_edge(G, i, bi+N, 1) #  仲良しペアを作ることができるので辺を作成

    ans = max_flow(G, 2*N+2, 0, 2*N+1) #  ソースとシンク間の最大流
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
