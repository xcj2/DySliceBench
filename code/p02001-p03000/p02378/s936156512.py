class Node():
    def __init__(self):
        self.edge = []
        self.level = None
        self.par = None
        self.cap = 10**18

class Edge():
    def __init__(self, to, cap, rev=None):
        self.to = to
        self.cap = cap
        self.rev = rev

from collections import deque

class BipartiteMatching():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.inf = 10**18
        self.source = Node()
        self.sink = Node()
        self.lt = [Node() for _ in range(n)]
        self.rt = [Node() for _ in range(m)]
        for i in range(n):
            edge = Edge(self.lt[i], 1)
            rev = Edge(self.source, 0)
            edge.rev, rev.rev = rev, edge
            self.source.edge.append(edge)
            self.lt[i].edge.append(rev)
        for i in range(m):
            edge = Edge(self.sink, 1)
            rev = Edge(self.rt[i], 0)
            edge.rev, rev.rev = rev, edge
            self.rt[i].edge.append(edge)
            self.sink.edge.append(rev)

    def add(self, x, y):
        lt = self.lt[x]
        rt = self.rt[y]
        edge = Edge(rt, 1)
        rev = Edge(lt, 0)
        edge.rev, rev.rev = rev, edge
        lt.edge.append(edge)
        rt.edge.append(rev)

    def maximum_matching(self):
        flow = 0
        while True:
            queue = deque([self.source])
            self.source.level = 0
            self.sink.level = None
            for i in range(self.n):
                self.lt[i].level = None
            for i in range(self.m):
                self.rt[i].level = None
            while queue:
                node = queue.popleft()
                for edge in node.edge:
                    to = edge.to
                    if edge.cap and to.level is None:
                        to.level = node.level + 1
                        queue.append(to)
            if self.sink.level is None: break
            stack = [self.source]
            self.source.par = None
            self.sink.par = None
            for i in range(self.n):
                self.lt[i].par = None
            for i in range(self.m):
                self.rt[i].par = None
            while stack:
                node = stack.pop()
                if node is self.sink:
                    break
                for edge in node.edge:
                    to = edge.to
                    if edge.cap and node.level < to.level:
                        to.par = edge.rev
                        #to.cap = min(edge.cap, node.cap)
                        stack.append(to)
            node = self.sink
            delta = node.cap
            while node is not self.source:
                node.par.cap = 1
                node.par.rev.cap = 0
                node = node.par.to
            flow += 1
        return flow

import sys
input = sys.stdin.readline

N, M, E = map(int, input().split())
bm = BipartiteMatching(N, M)
for _ in range(E):
    x, y = map(int, input().split())
    bm.add(x, y)
print(bm.maximum_matching())
