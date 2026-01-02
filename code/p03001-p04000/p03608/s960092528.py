import sys
import heapq
import math
import itertools

input = sys.stdin.readline

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

N,M,rr = (int(i) for i in input().split())
R = [int(i)-1 for i in input().split()]
edges = []
for i in range(M):
    a,b,c = (int(i) for i in input().split())
    edges.append((a-1, b-1, c))

graph = make_Graph(N, edges)

r_edges = []
for r1 in R:
    d, prev = Dijkstra(graph, r1)
    for r2 in R:
        (a,b,c) = r1, r2, d[r2]
        r_edges.append((a,b,c))

r_graph = make_Graph(N, r_edges)

reslis = []
for LL in list(itertools.permutations(R)):
    res = 0
    for i in range(len(LL)-1):
        a, b = (LL[i], LL[i + 1])
        res += r_graph[a][b]
    reslis.append(res)

reslis.sort()
res = reslis[0]
print(res)
