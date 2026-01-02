#!/usr/bin/env pypy3


import heapq
import sys


M = 10 ** 15
INF = 10 * M


def dijkstra(num_vs, source, adj_vs, costs):
    min_dist = [INF for _ in range(num_vs)]
    min_dist[source] = 0
    pq = [(min_dist[i], i) for i in range(num_vs)]
    heapq.heapify(pq)
    while pq:
        min_dist_i, i = heapq.heappop(pq)
        for j in adj_vs[i]:
            new_length = min_dist[i] + costs[(i, j)]
            if new_length < min_dist[j]:
                min_dist[j] = new_length
                heapq.heappush(pq, (new_length, j))
    return min_dist


def max_values(n, s, t, adj_vs, yen_costs, snuke_costs):
    s_to_x_yen_dists = dijkstra(n, s, adj_vs, yen_costs)
    # s_to_x_snuke_dists = dijkstra(n, s, adj_vs, snuke_costs)
    # t_to_x_yen_dists = dijkstra(n, t, adj_vs, yen_costs)
    t_to_x_snuke_dists = dijkstra(n, t, adj_vs, snuke_costs)
    # 両替所 i を経由したときの残金
    p2r = [M - s_to_x_yen_dists[i] - t_to_x_snuke_dists[i] for i in range(n)]
    # print(p2r, file=sys.stderr)
    res = [p2r[n - 1]]
    for i in range(n - 1)[::-1]:
        new_r = p2r[i]
        if new_r > res[-1]:
            res.append(new_r)
        else:
            res.append(res[-1])
    res.reverse()
    # print(res, file=sys.stderr)
    return res


def main():
    n, m, s, t = (int(x) for x in input().split())
    s -= 1
    t -= 1
    yen_costs = dict()
    snuke_costs = dict()
    adj_vs = [set() for _ in range(n)]
    for _ in range(m):
        u, v, a, b = (int(x) for x in input().split())
        u -= 1
        v -= 1
        adj_vs[u].add(v)
        adj_vs[v].add(u)
        yen_costs[(u, v)] = yen_costs[(v, u)] = a
        snuke_costs[(u, v)] = snuke_costs[(v, u)] = b
    res = max_values(n, s, t, adj_vs, yen_costs, snuke_costs)
    for line in res:
        print(line)


if __name__ == '__main__':
    main()
