
import collections
import itertools
import sys

def getint(): return int(input())
def getints(): return list(map(int, input().split()))


class Graph:
    def __init__(self, node_count, edge_count):
        self.lst = [-1 for _ in range(node_count)]
        self.nxt = [0  for _ in range(edge_count)]
        self.to  = [0  for _ in range(edge_count)]
        self.m   =  0

    def add_edge(self, u, v, w):  # bidirection weight
        m = self.m
        self.nxt[m], self.lst[u], self.to[m]= self.lst[u], m, (v, w)
        self.m += 1

    def traverse(self,u):
        m = self.lst[u]
        while m != -1:
            yield self.to[m]
            m = self.nxt[m]

n,m=getints()
graph = Graph(n,2*m)
for i in range(m):
    a,b=getints()
    graph.add_edge(a-1,b-1,1)
    graph.add_edge(b-1,a-1,1)

visited = [False] * n

def solve(u, visited):
    if visited[u]:
        return 0
    visited[u]=True
    if all(visited):
        visited[u]=False
        return 1
    res = 0
    for v,_ in graph.traverse(u):
        res += solve(v, visited)
    visited[u]=False
    return res

print(solve(0, visited))