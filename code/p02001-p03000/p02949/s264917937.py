from collections import deque

class GraphWeighted(): #directed
    def __init__(self,n,edge):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.deg = [0 for _ in range(n)]
        for e in edge:
            self.graph[e[0]-1].append((e[1]-1,e[2]))
            self.deg[e[1]-1] += 1
    def bellman_ford(self,s,INF=10**18):
        dist = [INF for _ in range(self.n)]
        dist[s] = 0
        update = True
        for i in range(self.n):
            update = False
            for node, g in enumerate(self.graph):
                for adj,adjcost in g:
                    if dist[node] != INF and dist[node]+adjcost < dist[adj]:
                        dist[adj] = dist[node]+adjcost
                        update = True
                        if i == self.n-1:
                            tmp = adj
            if not update:
                return dist
        visited = [0 for _ in range(self.n)]
        visited[tmp] = 1
        stack = [tmp]
        while stack:
            node = stack.pop()
            for adj,c in self.graph[node]:
                if not visited[adj]:
                    visited[adj] = 1
                    stack.append(adj)
        if visited[-1]:
            return -1
        else:
            return dist

class Graph(): #directed
    def __init__(self,n,edge):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.deg = [0 for _ in range(n)]
        for e in edge:
            self.graph[e[0]-1].append(e[1]-1)
            self.deg[e[1]-1] += 1
    def BFS(self,s):
        dist = [None for _ in range(self.n)]
        dist[s] = 0
        queue = deque([s])
        while queue:
            node = queue.popleft()
            for adj in self.graph[node]:
                if dist[adj] is not None:
                    continue
                dist[adj] = dist[node]+1
                queue.append(adj)
        return dist

INF = 10**18

N,M,P = map(int,input().split())
E = [tuple(map(int,input().split())) for _ in range(M)]

rev = []
for e in E:
    rev.append((e[1],e[0]))

R = Graph(N,rev)
reachable = R.BFS(N-1)

edge = []
for e in E:
    if reachable[e[0]-1] is None or reachable[e[1]-1] is None:
        continue
    edge.append((e[0],e[1],P-e[2]))

G = GraphWeighted(N,edge)
A = G.bellman_ford(0)

print(max(-A[-1],0) if A!=-1 else -1)