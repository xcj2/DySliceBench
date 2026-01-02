from collections import defaultdict
import heapq
n, m, s, t = map(int, input().split())


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))


class Dijkstra():
    def __init__(self, graph, start):
        self.g = graph.graph
        self.dist = defaultdict(lambda: float("inf"))
        self.dist[start] = 0
        self.prev = defaultdict(lambda: None)
        self.queue = []
        heapq.heappush(self.queue, (self.dist[start], start))

        while self.queue:
            dist_u, u = heapq.heappop(self.queue)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heapq.heappush(self.queue, (alt, v))


    def shortest_dist(self, goal):
        return self.dist[goal]

    
    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


yen_max = 10 ** 15
cost = [0] * n
train_yen = Graph()
train_sno = Graph()
for i in range(m):
    u, v, a, b = map(int, input().split())
    train_yen.add_edge(u - 1, v - 1, a)
    train_yen.add_edge(v - 1, u - 1, a)
    train_sno.add_edge(u - 1, v - 1, b)
    train_sno.add_edge(v - 1, u - 1, b)

cost_yen = Dijkstra(train_yen, s - 1)
cost_sno = Dijkstra(train_sno, t - 1)
for i in range(n):
    cost[i] = yen_max - (cost_yen.dist[i] + cost_sno.dist[i])

ans = [yen_max] * n
ans[n - 1] = cost[n - 1]
for i in range(n - 2, -1, -1):
    ans[i] = max(ans[i + 1], cost[i])
print(*ans, sep="\n")