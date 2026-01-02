#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	diameter_of_a_tree
# CreatedDate:  2020-07-10 20:12:23 +0900
# LastModified: 2020-07-29 00:12:01 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from collections import deque


class Graph():
    def __init__(self, vertex):
        self.V = vertex
        self.path = [[] for _ in range(self.V)]
        self.distance = [0] * self.V
        self.Q = deque()

    def addedge(self, s, t, w):
        self.path[s].append([w, t])
        self.path[t].append([w, s])

    def bfs(self, init):
        prev = init
        self.Q.append([init, prev])
        while self.Q:
            u, prev = self.Q.popleft()
            for w, v in self.path[u]:
                if self.distance[u] + w > self.distance[v] and prev != v:
                    self.distance[v] = self.distance[u] + w
                    self.Q.append([v, u])

        return max(self.distance), self.distance.index(max(self.distance))

    def clear(self):
        self.distance = [0] * self.V


def main():
    n = int(input())
    graph = Graph(n)
    for _ in range(n-1):
        s, t, w = map(int, input().split())
        graph.addedge(s, t, w)
    _, nt = graph.bfs(0)
    graph.clear()
    ans, _ = graph.bfs(nt)
    print(ans)


'''
    for init in range(n):
        ans = max(ans, graph.bfs(init))
        graph.clear()
'''
    

if __name__ == "__main__":
    main()

