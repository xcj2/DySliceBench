#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect
import queue

class Graph:

    def __init__(self, size):
        # id starts from 0
        self.size = size
        self.vertices = [0] * size # indicate parent
        self.visited = [False] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = []

    def add_edge(self, frm, to):
        self.edges[frm].append(to)
        self.edges[to].append(frm)


class Solver:

    def __init__(self, graph):
        self.graph = graph
        self.que = queue.Queue() # (to, parent)
        self.set(0, -1)

    def set(self, v, parent):
        self.que.put(v)
        self.graph.visited[v] = True
        self.graph.vertices[v] = parent

    def run(self):
        while not self.que.empty():
            parent = self.que.get()
            for to in self.graph.edges[parent]:
                if self.graph.visited[to]:
                    continue
                self.set(to, parent)
        self.print_ans()

    def print_ans(self):
        #print('self.graph.parent') # debug
        #print(self.graph.vertices) # debug
        print("Yes")
        for parent in self.graph.vertices[1:]:
            print(parent + 1)

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    graph = Graph(n)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        graph.add_edge(a, b)
    Solver(graph).run()

    #print('\33[32m' + 'end' + '\033[0m') # debug
