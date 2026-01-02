from collections import deque

class Graph():
    def __init__(self, directed:bool, nord_count:int):
        self.directed = directed
        self.degree = [0 for _ in range(nord_count)]
        self.edges = [[] for _ in range(nord_count)]
        self.edge_count = 0
        self.nord_count = nord_count


    def insert_edge(self, x, y, directed:bool):
        edge = EdgeNode(y=y, weight=None, edge_node = None)
        self.edges[x].append(edge)
        self.degree[x] += 1
        if directed == False:
            self.insert_edge(y, x, True)
        else:
            self.edge_count += 1

    def print_graph(self):
        for i in range(self.nord_count):
            for edge in self.edges[i]:
                print(i, edge.y)

class EdgeNode():
    def __init__(self, y, weight, edge_node):
        self.y = y
        self.weight = weight
        self.edge_node = edge_node

N, M = [int(i) for i in input().split()]
graph = Graph(directed=False, nord_count = N)
for i in range(M):
    A, B  = [int(i) for i in input().split()]
    graph.insert_edge(x=A-1, y=B-1, directed=False)

signpost = [None for _ in range(N)]
found = [False for _ in range(N)]
found[0] = True
current_node = 0
previous_node = 0
queue = deque([[previous_node, current_node]])
while len(queue) != 0:
    previous_node, current_node = queue.popleft()
    signpost[current_node] = previous_node
    for edge in graph.edges[current_node]:
        if found[edge.y] == False:
            found[edge.y] = True
            queue.append([current_node, edge.y])
signpost = signpost[1:]
if None in signpost:
    print('No')
else:
    print('Yes')
    for i in signpost:
        print(i+1)