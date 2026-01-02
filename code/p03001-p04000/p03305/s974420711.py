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

n, m, s, t = li()
s -= 1
t -= 1

yen_graph = [[] for _ in range(n)]
snk_graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, a, b = li()
    u -= 1
    v -= 1

    yen_graph[u].append((v, a))
    yen_graph[v].append((u, a))
    snk_graph[u].append((v, b))
    snk_graph[v].append((u, b))

yen_dist = dijkstra(yen_graph, s)
snk_dist = dijkstra(snk_graph, t)

initial = 10**15

ans = [-1]*n
for i in range(n-1, -1, -1):
    if i == n-1:
        ans[i] = initial - (yen_dist[i] + snk_dist[i])

    else:
        ans[i] = max(ans[i+1], initial - (yen_dist[i] + snk_dist[i]))

for ansi in ans:
    print(ansi)