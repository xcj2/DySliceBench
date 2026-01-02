#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array
import collections
import heapq


G_INF = 2 ** 31


class Dijkstra(object):

    def __init__(self, number_of_vertices, adjacency_list, costs, start):
        self.max_v = number_of_vertices
        self.adj = adjacency_list
        self.costs = costs
        self.start = start
        self.dist = None

    def initialize_dist(self):
        self.dist = collections.defaultdict(lambda: G_INF)
        self.dist[self.start] = 0

    def single_source_shortest_path(self):
        self.initialize_dist()
        pq = [(self.dist[v], v) for v in range(self.max_v)]
        heapq.heapify(pq)
        while pq:
            (_, v) = heapq.heappop(pq)
            for u in self.adj[v]:
                new_length = self.dist[v] + self.costs[(v, u)]
                if new_length < self.dist[u]:
                    self.dist[u] = new_length
                    heapq.heappush(pq, (new_length, u))
        return self.dist


def main():
    max_v, max_e, start = map(int, input().split())
    adjacency_list = collections.defaultdict(lambda: array.array("L"))
    costs = collections.defaultdict(lambda: G_INF)
    for _ in range(max_e):
        s, t, d = map(int, input().split())
        adjacency_list[s].append(t)
        costs[(s, t)] = d
    dij = Dijkstra(max_v, adjacency_list, costs, start)
    dist = dij.single_source_shortest_path()
    for v in range(max_v):
        result = dist[v]
        if result < G_INF:
            print(result)
        else:
            print("INF")


if __name__ == '__main__':
    main()