import heapq
import math

def make_Graph(N, edges):#頂点の名前はi - 1で受け付ける
    graph = {}
    for i in range(N):
        graph[i] = {}
        for j in range(N):
            graph[i][j] = 0
    for edge in edges:
        a, b, c = edge
        graph[a][b] = c
        graph[b][a] = c
    return graph

def Dijkstra(graph, start):
    N = len(graph)
    d = {}
    prev = {}
    for i in range(N):
        prev[i] = None
        if i == start:
            d[i] = 0
        else:
            d[i] = float('inf')
    Q = []
    heapq.heappush(Q, (0, start))
    while Q:
        d_u, u = heapq.heappop(Q)
        if d[u] < d_u:#ダブりを回避
            continue
        for i in range(N):
            if graph[u][i]:
                temp = d_u + graph[u][i]
                if d[i] > temp:
                    d[i] = temp
                    prev[i] = u
                    heapq.heappush(Q, (d[i], i))
    return (d, prev)

def saitan(start, goal, d, prev):
    temp = goal
    res = [goal]
    while True:
        res.append(prev[temp])
        if prev[temp] == start:
            break
        else:
            temp = prev[temp]
    return res

N,M = (int(i) for i in input().split())
edges = []
for i in range(M):
    a,b,c = (int(i) for i in input().split())
    edges.append((a-1, b-1, c))

graph = make_Graph(N, edges)

res = []
for i in range(N):
    d, prev = Dijkstra(graph, i)
    for j in range(N):
        if i != j:
            sait = saitan(i, j, d, prev)
            for k in range(len(sait) - 1):
                res.append(  (min(sait[k], sait[k + 1]) , max(sait[k], sait[k + 1]) ) )

res = set(res)
print(M - len(res))