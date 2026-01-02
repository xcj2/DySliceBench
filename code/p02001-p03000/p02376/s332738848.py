#!/usr/bin/env python3
# Based on
# https://en.wikipedia.org/wiki/Ford???Fulkerson_algorithm
# http://algoogle.hadrori.jp/algorithm/ford-fulkerson.html

import array
import collections
import sys


REC_LIMIT = 10000
INF = 10 ** 8


Edge = collections.namedtuple("Edge", "source sink capacity")


class FlowNetwork(object):

    def __init__(self, num_vertices):
        self.adj_edges = [set() for _ in range(num_vertices)]
        self.flow = None
        self.rev_edge = dict()
        self.used = None

    def get_edges_from(self, vertex):
        return self.adj_edges[vertex]

    def add_edge(self, source, sink, capacity):
        assert source != sink
        forward_edge = Edge(source, sink, capacity)
        backward_edge = Edge(sink, source, 0)
        self.rev_edge[forward_edge] = backward_edge
        self.rev_edge[backward_edge] = forward_edge
        self.adj_edges[source].add(forward_edge)
        self.adj_edges[sink].add(backward_edge)

    def dfs(self, source, sink, flow):
        if source == sink:
            return flow
        self.used[source] = True
        for edge in self.get_edges_from(source):
            rest = edge.capacity - self.flow[edge]
            if self.used[edge.sink] or rest <= 0:
                continue
            d = self.dfs(edge.sink, sink, min(flow, rest))
            if d > 0:
                self.flow[edge] += d
                self.flow[self.rev_edge[edge]] -= d
                return d
        return 0

    def ford_fulkerson(self, source, sink):
        self.flow = collections.defaultdict(int)
        max_flow = 0
        while True:
            self.used = collections.defaultdict(bool)
            df = self.dfs(source, sink, INF)
            if df == 0:
                return max_flow
            else:
                max_flow += df


def main():
    sys.setrecursionlimit(REC_LIMIT)
    v, e = map(int, input().split())
    network = FlowNetwork(v)
    for _ in range(e):
        network.add_edge(*map(int, input().split()))
    mf = network.ford_fulkerson(0, v - 1)
    print(mf)


if __name__ == '__main__':
    main()