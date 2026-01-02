# -*- coding: utf-8 -*-
"""
Matching - Bipartite Matching
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_7_A&lang=jp

"""
import sys
from sys import stdin
from collections import namedtuple
input = stdin.readline
edge = namedtuple('edge', ['to', 'cap', 'rev'])


def add_edge(G, f, t, c):
    G[f].append(edge(t, c, len(G[t])))
    G[t].append(edge(f, 0, len(G[f]) - 1))


def dfs(G, used, v, t, f):
    if v == t:
        return f
    used[v] = True
    for i in range(len(G[v])):
        e = G[v][i]
        if (not used[e.to]) and (e.cap > 0):
            d = dfs(G, used, e.to, t, min(f, e.cap))
            if d > 0:
                G[v][i] = edge(e.to, e.cap - d, e.rev)
                G[e.to][e.rev] = edge(G[e.to][e.rev].to, G[e.to][e.rev].cap + d, G[e.to][e.rev].rev)
                return d
    return 0


def max_flow(G, V, s, t):
    flow = 0
    while True:
        used = [False] * V
        f = dfs(G, used, s, t, float('inf'))
        if f == 0:
            return flow
        flow += f


def main(args):
    """
    - 追加したソースノードID: 0
    - Xグループ: 1〜X
    - Yグループ: X+1〜X+Y
    - 追加したシンクノードID: X+Y+1
    として、ノード0 → X+Y+1 への最大流を求める
    """
    X, Y, E = map(int, input().split())
    G = [[] for _ in range(X+Y+2)]

    for li in range(E):
        x, y = map(int, input().split())
        add_edge(G, x+1, X+y+1, 1)

    for x in range(1, X+1):
        add_edge(G, 0, x, 1)       # ソースから集合X
    for y in range(X+1, X+Y+1):
        add_edge(G, y, X+Y+1, 1)   # 集合Yからシンク


    ans = max_flow(G, X+Y+2, 0, X+Y+1) #  ソースとシンク間の最大流
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])


