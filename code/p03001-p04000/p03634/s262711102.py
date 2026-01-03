import sys
input = sys.stdin.readline

def make_Graph(N, edges):#頂点の名前はi - 1で受け付ける
    graph = [ [] for i in range(N)]
    for edge in edges:
        a, b, c = edge
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph

def BFS(N, graph, start):
    Q = []
    V = []
    prev = [None] * N
    dd = [float("inf")] * N
    Q.append(start)
    dd[start] = 0
    while len(V) < N:
        a = Q.pop(0)
        V.append(a)
        for b, c in graph[a]:
            if b != prev[a]:
                Q.append(b)
                prev[b] = a
                dd[b] = dd[a] + c
    return dd

def DFS(N, graph, a, p, d):
    dd[a] = d
    for b, c in graph[a]:
        if b == p or dd[b] != 0:
            continue
        else:
            DFS(N, graph, b, a, d + c)

N = int(input())

sys.setrecursionlimit(100)

graph = [ [] for i in range(N)]
for i in range(N-1):
    a, b, c = (int(j) for j in input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

Q, K =(int(i) for i in input().split())
dd = [0] * N

try:
    DFS(N, graph, K-1, -1, 0)
except:
    dd = BFS(N, graph, K-1)

for i in range(Q):
    x, y = (int(a) for a in input().split())
    print(dd[x-1] + dd[y-1])