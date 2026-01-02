#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	bridges
# CreatedDate:  2020-07-26 23:07:19 +0900
# LastModified: 2020-07-26 23:42:02 +0900
#


import os
import sys
sys.setrecursionlimit(100000)

# import numpy as np
# import pandas as pd


class Graph():
    def __init__(self, V):
        self.V = V
        self.path = [[] for _ in range(self.V)]
        self.parents = [-1] * self.V
        self.lowlink = [float('inf')] * self.V
        self.order = [float('inf')] * self.V
        self.ap = []

    def add(self, s, t):
        self.path[s].append(t)
        self.path[t].append(s)

    def dfs(self, k, u):
        child = 0
        self.lowlink[u] = k
        self.order[u] = k
        k += 1
        for v in self.path[u]:
            if self.lowlink[v] == float('inf'):
                child += 1
                self.parents[v] = u
                self.dfs(k, v)
                self.lowlink[u] = min(self.lowlink[u], self.lowlink[v])

                if self.lowlink[v] > self.order[u]:
                    self.ap.append(sorted([u, v]))

            elif self.parents[u] != v:
                self.lowlink[u] = min(self.lowlink[u], self.order[v])

    def lowlink_order_print(self):
#        print("lowlink:", self.lowlink)
#        print("order:", self.order)
        self.ap = sorted(self.ap)
        for s in self.ap:
            print("{} {}".format(s[0], s[1]))


def main():
    V, E = map(int, input().split())
    graph = Graph(V)
    for _ in range(E):
        s, t = map(int, input().split())
        graph.add(s, t)
    graph.dfs(0, 0)
    graph.lowlink_order_print()


if __name__ == "__main__":
    main()

