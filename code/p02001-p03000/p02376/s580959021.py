# -*- coding: utf-8 -*-
"""
Network Flow - Maximum Flow
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp

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


def max_flow(G, V,s, t):
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
    V, E = map(int, input().split())

    G = [[] for _ in range(V)]
    for _ in range(E):
        u, v, c = map(int, input().split())
        add_edge(G, u, v, c)

    ans = max_flow(G, V, 0, V - 1)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])

