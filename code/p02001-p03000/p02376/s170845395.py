class Edge():
    def __init__(self, to, cap, rev=None):
        self.to = to
        self.cap = cap
        self.rev = rev

from collections import deque

class Dinic():
    def __init__(self, n):
        self.n = n
        self.inf = 10**18
        self.graph = [[] for _ in range(self.n)]

    def add(self, fr, to, cap):
        edge = Edge(to, cap)
        rev = Edge(fr, 0)
        edge.rev, rev.rev = rev, edge
        self.graph[fr].append(edge)
        self.graph[to].append(rev)

    def max_flow(self, source, sink):
        flow = 0
        while True:
            queue = deque([source])
            level = [None for _ in range(self.n)]
            level[source] = 0
            while queue:
                node = queue.popleft()
                for edge in self.graph[node]:
                    to = edge.to
                    if edge.cap and level[to] is None:
                        level[to] = level[node] + 1
                        queue.append(to)
            if level[sink] is None: break
            stack = [source]
            par = [None for _ in range(self.n)]
            par[source] = source
            cap = [self.inf for _ in range(self.n)]
            while stack:
                node = stack.pop()
                if node == sink:
                    break
                for edge in self.graph[node]:
                    to = edge.to
                    if edge.cap and level[node] < level[to]:
                        par[to] = node
                        cap[to] = min(edge.cap, cap[node])
                        stack.append(to)
            node = sink
            prev = par[sink]
            delta = cap[sink]
            while node != source:
                for edge in self.graph[prev]:
                    if edge.to == node:
                        edge.cap -= delta
                        edge.rev.cap += delta
                node = prev
                prev = par[node]
            flow += delta
        return flow

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = Dinic(N)

for _ in range(M):
    u, v, c = map(int, input().split())
    d.add(u, v, c)

print(d.max_flow(0, N - 1))
