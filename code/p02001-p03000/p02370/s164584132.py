# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B&lang=jp

"""
import sys
from collections import deque


def bfs(u, result, out_edge, in_degree, processed):
    q = deque()
    q.append(u)
    processed[u] = True
    while q:
        u = q.popleft()
        result.append(u)
        for e in out_edge[u]:
            in_degree[e] -= 1
            if in_degree[e] == 0 and processed[e] == False:
                processed[e] = True
                q.append(e)





def solve(V, in_degree, out_edge):
    result = []
    processed = [False for _ in range(V)]

    for i, u in enumerate(in_degree):
        if u == 0 and processed[i] == False:
            bfs(i, result, out_edge, in_degree, processed)
    return result


def main(args):
    V, E = [int(x) for x in input().split(' ')]
    in_degree = [0 for _ in range(V)]
    out_edge = [[] for _ in range(V)]
    for _ in range(E):
        s, t = [int(x) for x in input().split(' ')]
        out_edge[s].append(t)
        in_degree[t] += 1

    result = solve(V, in_degree, out_edge)
    print('\n'.join(map(str, result)))


if __name__ == '__main__':
    main(sys.argv[1:])