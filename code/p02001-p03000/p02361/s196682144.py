import heapq
from enum import Enum, auto

class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()

class Node:
    def __init__(self, n, w):
        self.n = n
        self.w = w

    def __lt__(self, node):
        return self.w < node.w

color = []      # 探索状態
d = []          # コスト

# input
V, E, r = list(map(int, input().split(' ')))
adj_list = [[] for i in range(V)]
for i in range(E):
    s, t, d = list(map(int, input().split(' ')))
    adj_list[s].append([t, d])

def dijkstra(s):
    global d, color
    color = [Color.WHITE for i in range(V)]
    d = [float('inf') for i in range(V)]
    d[s] = 0

    pqueue = [Node(s, 0)]
    while len(pqueue) >= 1:
        u = heapq.heappop(pqueue).n
        color[u] = Color.BLACK

        for v, w in adj_list[u]:
            if color[v] != Color.BLACK:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    color[v] = Color.GRAY
                    heapq.heappush(pqueue, Node(v, d[v]))

dijkstra(r)
for w in d:
    if w == float('inf'):
        print('INF')
    else:
        print(w)

