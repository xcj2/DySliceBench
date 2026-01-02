#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	cycle_detection
# CreatedDate:  2020-07-28 21:10:00 +0900
# LastModified: 2020-07-28 21:57:12 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


class Graph():
    def __init__(self, vertex):
        self.V = vertex
        self.path = [[] for _ in range(self.V)]
        self.visited = [False] * self.V
        self.recurbox = [False] * self.V

    def addedge(self, s, t):
        self.path[s].append(t)

    def dfs(self, u):
        self.visited[u] = True
        self.recurbox[u] = True
        for v in self.path[u]:
            if self.visited[v] is False:
                if self.dfs(v) is True:
                    return True
            elif self.recurbox[v] is True:
                return True
        self.recurbox[u] = False
        return False

    def dfsutil(self):
        for i in range(self.V):
            if self.visited[i] is False:
                if self.dfs(i) is True:
                    return True
        return False


def main():
    V, E = map(int, input().split())
    graph = Graph(V)
    for _ in range(E):
        s, t = map(int, input().split())
        graph.addedge(s, t)
    if graph.dfsutil() is True:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()

