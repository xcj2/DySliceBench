from queue import Queue

class Graph():
    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, v):
        self.adjacency_dict[v] = {}
        
    def add_edge(self, v1, v2):
        self.adjacency_dict[v1][v2] = -1
        self.adjacency_dict[v2][v1] = -1
    
    def paint(self, v1, v2, color):
        self.adjacency_dict[v1][v2] = color
        self.adjacency_dict[v2][v1] = color
        
    def get_color(self, v1, v2):
        return self.adjacency_dict[v1][v2]
    
    def next_vertices(self, v):
        return self.adjacency_dict[v]


N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]


tree = Graph()
for i in range(1, N+1):
    tree.add_vertex(i)
for a,b in edges:
    tree.add_edge(a, b)

most_edges_vertex = -1
max_colors = 0
for k,v in tree.adjacency_dict.items():
    if len(v) > max_colors:
        most_edges_vertex = k
        max_colors = len(v)


# BFS
q = Queue()
q.put([most_edges_vertex, -1])  # [vertex, prev_color]
while not q.empty():
    vertex, prev_color = q.get()
    nexts = tree.next_vertices(vertex)
    color = 1 if prev_color != 1 else 2

    for v,c in nexts.items():
        if c > 0:
            continue
        q.put([v, color])
        
        # 色ぬり
        tree.paint(vertex, v, color)
        
        # 次の色
        color += 1
        if color == prev_color:
            color += 1

print(max_colors)
for v1,v2 in edges:
    print(tree.get_color(v1, v2))