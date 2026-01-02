from collections import defaultdict
from heapq import heappop, heappush


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):

    def __init__(self, graph, start):
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]

n,m,s,t = map(int, input().split())
uvab = [list(map(int, input().split())) for i in range(m)]
Ga = Graph()
Gb = Graph()
for u,v,a,b in uvab:
  Ga.add_edge(u-1,v-1,a)
  Ga.add_edge(v-1,u-1,a)
  Gb.add_edge(u-1,v-1,b)
  Gb.add_edge(v-1,u-1,b)
dist_a = Dijkstra(Ga,s-1)
dist_b = Dijkstra(Gb,t-1)
cost = 10 ** 18
money = 10 ** 15
ans = []
for i in range(n-1,-1,-1):
  tmp = dist_a.shortest_distance(i) + dist_b.shortest_distance(i)
  cost = min(cost, tmp)
  ans.append(cost)
for i in reversed(ans):
  print(money - i)