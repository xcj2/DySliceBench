import heapq
import sys
input = sys.stdin.readline

INF = 10 ** 18

class Edge():
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
    def __str__(self):
        return 'Edge: {} -> {}, cost {}'.format(self.start, self.end, self.cost)

def dijkstra(n, G, s):
    dist = [[INF, INF, INF] for _ in range(n)]
    dist[s][0] = 0
    h = []
    heapq.heappush(h, (0, s))

    while h:
        # 使っていない頂点のうち、現時点で最も距離の近いものを選びvとする
        d, v = heapq.heappop(h)
        if dist[v][d%3] < d:
            continue
        # vから到達可能な頂点について、距離が短くなれば更新
        for e in G[v]:
            tmp = dist[v][d%3] + e.cost
            if dist[e.end][tmp%3] > tmp:
                dist[e.end][tmp%3] = tmp
                heapq.heappush(h, (dist[e.end][tmp%3], e.end))
    return dist

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(Edge(u-1, v-1, 1))

s, t = map(int, input().split())

dist = dijkstra(n, g, s-1)
ans = dist[t-1][0]

if ans == INF:
    print(-1)
else:
    print(ans//3)

