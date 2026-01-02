import sys
sys.setrecursionlimit(100000)

class Graph():
    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, v):
        self.adjacency_dict[v] = []
    
    def add_edge(self, v1, v2, dist):
        self.adjacency_dict[v1].append([v2, dist])
        self.adjacency_dict[v2].append([v1, dist])
    
    def next_edges(self, v):
        return self.adjacency_dict[v]

N = int(input())
dists = [list(map(int, input().split())) for _ in range(N-1)]

graph = Graph()
for i in range(1, N+1):
    graph.add_vertex(i)
for v1, v2, dist in dists:
    graph.add_edge(v1, v2, dist)

def dfs(start, group):
    if visited[start] is not None:
        return
    visited[start] = group
    for v, dist in graph.next_edges(start):
        if dist % 2 == 0:
            dfs(v, group)
        else:
            dfs(v, 1-group)

visited = [None]*(N+1)
dfs(1, 0)
for i in visited[1:]:
    print(i)