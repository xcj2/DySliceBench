import heapq

INF = float('inf')

class Edge():
    def __init__(self, a, b, cost):
        self.a = a
        self.b = b
        self.cost = cost
    def __str__(self):
        return 'Edge: {} -> {}, cost {}'.format(self.a, self.b, self.cost)

def dijkstra(n, G, s):
    dist = [INF] * n
    dist[s] = 0
    h = []
    heapq.heappush(h, (0, s))

    while h:
        # 使っていない頂点のうち、現時点で最も距離の近いものを選びvとする
        d, v = heapq.heappop(h)
        if dist[v] < d:
            continue
        # vから到達可能な頂点について、距離が短くなれば更新
        for e in G[v]:
            if dist[e.b] > dist[v] + e.cost:
                dist[e.b] = dist[v] + e.cost
                heapq.heappush(h, (dist[e.b], e.b))
    return dist

n, x, y = map(int, input().split())

g = [[] for i in range(n)]

for i in range(n-1):
    g[i].append(Edge(i, i+1, 1))
    g[i+1].append(Edge(i+1, i, 1))

g[x-1].append(Edge(x-1, y-1, 1))
g[y-1].append(Edge(y-1, x-1, 1))

ans = [0] * n

for i in range(n):
    for d in dijkstra(n, g, i):
        ans[d] += 1

for item in ans[1:]:
    print(item // 2)

