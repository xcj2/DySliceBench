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
            if dist[e.end] > dist[v] + e.cost:
                dist[e.end] = dist[v] + e.cost
                heapq.heappush(h, (dist[e.end], e.end))
    return dist


n = int(input())
es = [[] for i in range(n)]

for i in range(n-1):
    a, b, c = list(map(int, input().split()))
    es[a-1].append(Edge(a-1, b-1, c))
    es[b-1].append(Edge(b-1, a-1, c))

q, k = map(int, input().split())
k -= 1

d = dijkstra(n, es, k)

for j in range(q):
    x, y = map(int, input().split())
    print(d[x-1] + d[y-1])


