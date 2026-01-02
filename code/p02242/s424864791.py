from collections import namedtuple
import heapq

Edge = namedtuple('Edge', ('fr', 'to', 'cost'))
inf = int(1e9)


def bellman_ford(n, start, edges):
    dists = [inf for _ in range(n)]
    dists[start] = 0
    while True:
        updated = False
        for e in edges:
            if dists[e.fr] != inf and dists[e.fr] + e.cost < dists[e.to]:
                updated = True
                dists[e.to] = dists[e.fr] + e.cost

        if not updated:
            break

    return dists


def dijkstra(n, costs):
    dists = [inf for _ in range(n)]
    dists[0] = 0

    queue = []
    for (i, d) in enumerate(dists):
        heapq.heappush(queue, (d, i))

    while len(queue) > 0:
        d, i = heapq.heappop(queue)
        if d > dists[i]:
            continue

        for v in range(n):
            if v == i or costs[i][v] == inf:
                continue

            if dists[i] + costs[i][v] < dists[v]:
                dists[v] = dists[i] + costs[i][v]
                heapq.heappush(queue, (dists[v], v))

    return dists


def warshall_floyd(n, costs):
    dists = [[costs[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

    return dists


n = int(input())

m = [[inf if i != j else 0 for i in range(n)] for j in range(n)]
es = []
for i in range(n):
    fs = list(map(int, input().split()))
    ne = fs[1]
    for j in range(ne):
        v = fs[2+2*j]
        c = fs[2+2*j+1]
        m[i][v] = c
        es.append(Edge(i, v, c))


# d = bellman_ford(n, 0, es)
# d = dijkstra(n, m)
d = warshall_floyd(n, m)
for (i, di) in enumerate(d[0]):
    print(i, di)


