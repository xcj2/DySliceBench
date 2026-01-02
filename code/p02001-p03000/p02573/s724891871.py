from collections import deque

class Graph():
    def __init__(self):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}

    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []
    def add_edge(self, v1, v2):
        """ ノード同士をつなぐ。"""
        # 無向グラフの場合は双方向。もし有向グラフなら片側のみ。
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)
    def next_vertices(self, v):
        """ 隣接したノードを返す """
        return self.adjacency_dict[v]

def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)

    group_size = 1
    while q:
        v_now = q.popleft()
        for v_next in graph.next_vertices(v_now):
            if visited[v_next] == False:
                visited[v_next] = True
                q.append(v_next)
                group_size += 1

    return group_size
    

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

graph = Graph()
for i in range(1, N+1):
    graph.add_vertex(i)
for v1, v2 in AB:
    graph.add_edge(v1, v2)

visited = [False] * (N+1)

max_group_size = 1
for i in range(1, N+1):
    if visited[i] == False:
        group_size = bfs(i)
        max_group_size = max(max_group_size, group_size)
    
print(max_group_size)