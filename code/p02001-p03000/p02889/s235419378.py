import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


from heapq import heappush, heappop


def dijkstra(graph: list, start, INF=float('inf')) -> list:
    n = len(graph)
    dist = [INF] * n
    visited = [False] * n

    dist[start] = 0
    que = [(0, start)]

    while que:
        cost, cur = heappop(que)

        if visited[cur]:
            continue

        visited[cur] = True

        for nextnode, edgecost in graph[cur]:
            nextcost = cost + edgecost
            if nextcost < dist[nextnode]:
                dist[nextnode] = nextcost
                heappush(que, (nextcost, nextnode))

    return dist

n, m, l = li()
graph = [[] for _ in range(n)]
costgraph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = li()
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

for st in range(n):
    dist = dijkstra(graph, st)
    for ds in range(n):
        if st == ds:
            continue

        if dist[ds] <= l:
            costgraph[st].append((ds, 1))

q = ni()
INF = float("inf")

dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i] = dijkstra(costgraph, i, INF)

for _ in range(q):
    st, ds = li_()
    if dist[st][ds] == INF:
        print(-1)
    else:
        print(dist[st][ds] - 1)