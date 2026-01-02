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
    dist = [INF ] *n
    visited = [False ] *n

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


n, m = li()

graph = [[] for _ in range(3*n)]
for _ in range(m):
    u, v = li_()
    for i in range(3):
        graph[i*n + u].append([(i+1)%3 * n + v, 1])

s, t = li_()
INF = 1<<62
dist = dijkstra(graph, s, INF)

print(-1 if dist[t] == INF else dist[t] // 3)
