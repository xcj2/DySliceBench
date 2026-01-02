import heapq
import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')

class Edge():
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

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

n, m, p = map(int, input().split())

g1 = [[] for _ in range(n)]
g2 = [[] for _ in range(n)]
es = []

abc = []

for _ in range(m):
    a, b, c = map(int, input().split())
    abc.append((a-1, b-1, c))
    g1[a-1].append(Edge(a-1, b-1, 1))
    g2[b-1].append(Edge(b-1, a-1, 1))

dist1 = dijkstra(n, g1, 0)
dist2 = dijkstra(n, g2, n-1)

# print(dist1)
# print(dist2)

ng = set({})

for i in range(n):
    if dist1[i] == INF or dist2[i] == INF:
        ng.add(i)

for a, b, c in abc:
    if a in ng or b in ng:
        continue
    es.append(Edge(a, b, p-c))

def bellman_ford(n, es, s):
    dist = [INF] * n
    dist[s] = 0
    # 更新が止まるまで繰り返す O(V*E)
    # i度目の更新までにsを始点として0~i個の辺からなる経路が探索され、その時点の最短経路が計算される
    # 最短経路は最大でもV-1個の頂点しか通らないため、最悪でもv-1回で収束する
    while True:
        update = False
        # 辺をすべて見る
        for e in es:
            # aに到達可能かつa経由の方が近ければ更新する
            if dist[e.start] != INF and dist[e.end] > dist[e.start] + e.cost:
                dist[e.end] = dist[e.start] + e.cost
                update = True
        # 一度も更新されなければ終了
        if not update:
            break
    return dist

def find_negative_loop(n, es):
    dist = [0] * n
    for i in range(n):
        for e in es:
            if dist[e.end] > dist[e.start] + e.cost:
                dist[e.end] = dist[e.start] + e.cost
                if i == n - 1:
                    return True
    return False

if find_negative_loop(n, es):
    print(-1)
    sys.exit()

dist = bellman_ford(n, es, 0)
print(max(0, -dist[n-1]))
