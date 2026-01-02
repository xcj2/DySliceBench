#!/usr/bin/env python3

import sys
import heapq
from collections import namedtuple

DEBUG = False

def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep = " "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


edge = namedtuple("edge", ("cost", "to"))
vertex_route = namedtuple("vertex_route", ("routecost", "vertex"))

def main():
    v, e, r = read_list(int)
    edges_of_v = {}
    for _ in range(e):
        s, t, d = read_list(int)
        if s not in edges_of_v:
            edges_of_v[s] = []
        edges_of_v[s].append(edge(d, t))
    
    min_costs = [1 << 33] * v
    que = [vertex_route(0, r)]
    heapq.heapify(que)
    while que:
        route = heapq.heappop(que)
        if min_costs[route.vertex] <= route.routecost:
            continue
        min_costs[route.vertex] = route.routecost
        if route.vertex not in edges_of_v:
            continue
        for e in edges_of_v[route.vertex]:
            if min_costs[e.to] <= e.cost + min_costs[route.vertex]:
                continue
            heapq.heappush(que, vertex_route(e.cost + min_costs[route.vertex], e.to))
    
    for i in range(v):
        if min_costs[i] == 1 << 33:
            print("INF")
        else:
            print(min_costs[i])

if __name__ == "__main__":
    main()

