#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array
import collections
import heapq


AdjacentVertex = collections.namedtuple("AdjacentVertex", "vertex cost")
DIV = 100
INF = 2 ** 31 - 1


def compute_mst_prim(max_v, adj_list):
    key = collections.defaultdict(lambda: INF)
    key[0] = 0
    pq = [(key[v], v) for v in range(max_v)]
    heapq.heapify(pq)
    in_pq = array.array("B", (True for _ in range(max_v)))
    while pq:
        _, u = heapq.heappop(pq)
        in_pq[u] = False
        for v, v_cost in adj_list[u]:
            if in_pq[v]:
                w = v_cost
                if w < key[v]:
                    key[v] = w
                    heapq.heappush(pq, (w, v))
                    in_pq[v] = True
    return key


def compute_number_of_lanterns(max_v, adj_list):
    key = compute_mst_prim(max_v, adj_list)
    return sum(x - 1 for x in key.values() if x > 0)


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        m = int(input())
        adj_list = collections.defaultdict(set)
        for _ in range(m):
            a, b, w = map(int, input().split(","))
            adj_list[a].add((b, w // DIV))
            adj_list[b].add((a, w // DIV))
        print(compute_number_of_lanterns(n, adj_list))


if __name__ == '__main__':
    main()