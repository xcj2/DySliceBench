# -*- coding: utf-8 -*-
"""
http://abc067.contest.atcoder.jp/tasks/arc078_b

"""
import sys
from sys import stdin
from heapq import heappop, heappush
input = stdin.readline


def prepare_graph(edges, N):
    adj = [[] for _ in range(N+1)]
    for a, b in edges:
        adj[a].append([b, 1])
        adj[b].append([a, 1])
    return adj


def dijkstra(adj, s):
    # ダイクストラ法で始点からの距離を計算する
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * len(adj)
    d = [float('inf')] * len(adj)    # 始点からの距離 計算結果
    d[s] = 0                    #  始点から自身までの距離は0
    pq = []
    heappush(pq, (0, s))
    while pq:
        cost, u = heappop(pq)
        color[u] = BLACK
        if d[u] < cost:
            continue
        for v, cost in adj[u]:
            if color[v] == BLACK:
                continue
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                heappush(pq, (d[v], v))
                color[v] = GRAY
    return d                    #  計算した距離情報を返す


def solve(edges, N):
    adj = prepare_graph(edges, N)
    f_dist = dijkstra(adj, 1)
    s_dist = dijkstra(adj, N)

    f_point = 0
    s_point = 0
    for f, s in zip(f_dist[1:], s_dist[1:]):
        if f <= s:
            f_point += 1
        else:
            s_point += 1
    if f_point > s_point:
        return 'Fennec'
    else:
        return 'Snuke'


def main(args):
    edges = []
    N = int(input())
    for _ in range(1, N):
        a, b = map(int, input().split())
        edges.append([a, b])
    ans = solve(edges, N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
