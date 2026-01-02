from collections import deque


def bellman_ford(start: int, graph: list) -> list:
    """bellman-ford法: 始点startから各頂点への最短距離を求める(負辺OK)
    計算量: O(|E||V|)
    """
    INF = float("inf")
    n = len(graph)
    dist = [-INF] * n
    dist[start] = 0
    if n == 1:
        return False, [0]
    for _ in range(n - 1):
        update = False
        for v, edge in enumerate(graph):
            for nxt_v, cost in edge:
                if not (visited[nxt_v] and visited2[nxt_v]):
                    continue
                if dist[nxt_v] < dist[v] + cost:
                    dist[nxt_v] = dist[v] + cost
                    update = True
        if not update:
            break
    else:
        return True, dist
    return False, dist

def bellman_ford2(start: int, graph: list) -> list:
    """bellman-ford法: 始点startから各頂点への最短距離を求める(負辺OK)
    計算量: O(|E||V|)
    """
    INF = float("inf")
    n = len(graph)
    dist = [-INF] * n
    dist[start] = 0
    if n == 1:
        return False, [0]
    for _ in range(n + 100):
        update = False
        for v, edge in enumerate(graph):
            for nxt_v, cost in edge:
                if not (visited[nxt_v] and visited2[nxt_v]):
                    continue
                if dist[nxt_v] < dist[v] + cost:
                    dist[nxt_v] = dist[v] + cost
                    update = True
        if not update:
            break
    else:
        return True, dist
    return False, dist

n, m, p = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

graph = [[] for i in range(n)]
rev_graph = [[] for i in range(n)]
for a, b, cost in info:
    a -= 1
    b -= 1
    cost -= p
    graph[a].append((b, cost))
    rev_graph[b].append((a, cost))

visited = [False] * n
def dfs():
    q = deque([0])
    visited[0] = True
    while q:
        v = q.pop()
        for nxt_v, _ in graph[v]:
            if visited[nxt_v]:
                continue
            visited[nxt_v] = True
            q.append(nxt_v)
dfs()

visited2 = [False] * n
def dfs2():
    q = deque([n - 1])
    visited2[n - 1] = True
    while q:
        v = q.pop()
        for nxt_v, _ in rev_graph[v]:
            if visited2[nxt_v]:
                continue
            visited2[nxt_v] = True
            q.append(nxt_v)
dfs2()

#print(visited)
#print(visited2)

boolian, dist = bellman_ford(0, graph)
boolian, dist2 = bellman_ford2(0, graph)
if not boolian:
    print(max(dist[-1], 0))
else:
    for i in range(n):
        if dist[i] < dist2[i]:
            print(-1)
            exit()
    print(dist2[-1])
        