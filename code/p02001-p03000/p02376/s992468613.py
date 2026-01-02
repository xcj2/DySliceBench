#!/usr/bin/env python3
# Based on ...
# https://en.wikipedia.org/wiki/Ford???Fulkerson_algorithm
# http://algoogle.hadrori.jp/algorithm/ford-fulkerson.html

import collections
import sys


REC_LIMIT = 10000
INF = 10 ** 8


class Edge(object):

    def __init__(self, source, sink, capacity):
        self.source = source
        self.sink = sink
        self.capacity = capacity
        self.rev_edge = None

    def __str__(self):
        return "Edge {} -> {} : {}".format(self.source,
                                           self.sink, self.capacity)


class FlowNetwork(object):

    def __init__(self):
        self.adj_edges = collections.defaultdict(list)
        self.flow = dict()
        self.used_edge = None

    def get_edges_from(self, vertex):
        return self.adj_edges[vertex]

    def add_edge(self, source, sink, capacity):
        assert source != sink
        f_edge = Edge(source, sink, capacity)
        b_edge = Edge(sink, source, 0)
        f_edge.rev_edge = b_edge
        b_edge.rev_edge = f_edge
        self.adj_edges[source].append(f_edge)
        self.adj_edges[sink].append(b_edge)
        self.flow[f_edge] = 0
        self.flow[b_edge] = 0

    def dfs(self, source, sink, flow):
        if source == sink:
            return flow
        self.used_edge[source] = True
        for edge in self.get_edges_from(source):
            residual = edge.capacity - self.flow[edge]
            if self.used_edge[edge.sink] or residual <= 0:
                continue
            d = self.dfs(edge.sink, sink, min(flow, residual))
            if d > 0:
                self.flow[edge] += d
                self.flow[edge.rev_edge] -= d
                return d
        return 0

    def ford_fulkerson(self, source, sink):
        max_flow = 0
        while True:
            self.used_edge = collections.defaultdict(bool)
            df = self.dfs(source, sink, INF)
            if df == 0:
                return max_flow
            else:
                max_flow += df


def main():
    sys.setrecursionlimit(REC_LIMIT)
    v, e = map(int, input().split())
    network = FlowNetwork()
    for _ in range(e):
        network.add_edge(*map(int, input().split()))
    mf = network.ford_fulkerson(0, v - 1)
    print(mf)


if __name__ == '__main__':
    main()