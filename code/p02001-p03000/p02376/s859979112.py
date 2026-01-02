# -*- coding: utf-8 -*-
"""
Network Flow - Maximum Flow
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp

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
    V, E = map(int, input().split())

    G = [[] for _ in range(V)]
    for _ in range(E):
        u, v, c = map(int, input().split())
        add_edge(G, u, v, c)

    ans = max_flow(G, V, 0, V - 1)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])

