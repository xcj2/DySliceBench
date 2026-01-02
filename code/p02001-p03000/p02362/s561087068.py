#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array
import collections


G_INF = 2 ** 31


class GraphError(Exception):
    pass


class GraphSearchError(GraphError):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return str(reason)


class ShortestPathFasterAlgorithm(object):

    def __init__(self, number_of_vertices, adjacency_list, costs, start):
        self.max_v = number_of_vertices
        self.adj = adjacency_list
        self.costs = costs
        self.start = start
        self.dist = None
        self.visits = None

    def initialize(self):
        self.dist = collections.defaultdict(lambda: G_INF)
        self.dist[self.start] = 0
        self.visits = collections.defaultdict(int)

    def single_source_shortest_path(self):
        self.initialize()
        q = collections.deque()
        q.append(self.start)
        while q:
            u = q.popleft()
            self.visits[u] += 1
            if self.visits[u] >= self.max_v:
                if self.max_v == 1:
                    return [0]
                raise GraphSearchError("A negative cycle was detected.")
            for v in self.adj[u]:
                new_length = self.dist[u] + self.costs[(u, v)]
                if new_length < self.dist[v]:
                    self.dist[v] = new_length
                    if v not in q:
                        q.append(v)
        return self.dist


def main():
    max_v, max_e, start = map(int, input().split())
    adjacency_list = collections.defaultdict(lambda: array.array("L"))
    costs = collections.defaultdict(lambda: G_INF)
    for _ in range(max_e):
        s, t, d = map(int, input().split())
        adjacency_list[s].append(t)
        costs[(s, t)] = d
    spfa = ShortestPathFasterAlgorithm(max_v, adjacency_list, costs, start)
    try:
        dist = spfa.single_source_shortest_path()
        for v in range(max_v):
            result = dist[v]
            if result < G_INF:
                print(result)
            else:
                print("INF")
    except GraphSearchError as gse:
        print("NEGATIVE CYCLE")


if __name__ == '__main__':
    main()