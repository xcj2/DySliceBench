# -*- coding: utf-8 -*-
"""
C - 2D Plane 2N Points
https://beta.atcoder.jp/contests/abc091/tasks/arc092_a

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
    used = [False] * V
    flow = 0
    while True:
        for i in range(len(used)):
            used[i] = False
        f = dfs(G, used, s, t, float('inf'))
        if f == 0:
            return flow
        flow += f


def main(args):
    N = int(input())
    G = [[] for _ in range(N*2 + 2)]
    red_points = []
    for ri in range(1, N+1):
        rx, ry = map(int, input().split())
        red_points.append([rx, ry])
        add_edge(G, 0, ri, 1)

    for bi in range(1, N+1):
        bx, by = map(int, input().split())
        add_edge(G, bi+N, N*2+1, 1)
        for i, r in enumerate(red_points, start=1):
            rx = r[0]
            ry = r[1]
            if rx < bx and ry < by:
                add_edge(G, i, bi+N, 1)

    ans = max_flow(G, 2*N+2, 0, 2*N+1)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
    
