
from collections import defaultdict
from heapq import heappop, heappush


class Graph():

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra():

    def __init__(self, graph, start):
        self.g = graph.graph

        self.dist = defaultdict(lambda: float("inf"))
        self.dist[start] = 0

        self.prev = defaultdict(lambda: None)

        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            dist_u, u = heappop(self.Q)

            if self.dist[u] < dist_u:
                continue

            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):

        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal

        while node is not None:
            path.append(node)
            node = self.prev[node]

        return path[::-1]


g=Graph()
n,m=map(int,input().split())
from collections import defaultdict
e=defaultdict(int)
for _ in range(m):
    a,b,c=map(int,input().split())
    g.add_edge(a,b,c)
    g.add_edge(b,a,c)
    a,b=min(a,b),max(a,b)
    e[(a,b)]+=1



d=[0]*(n+1)
d[0]=1
for i in range(1,n+1):
    dd=Dijkstra(g,i)
    for j in range(i+1,n+1):
        l=dd.shortest_path(j)
        for k in range(1,len(l)):
            a,b=min(l[k-1:k+1]),max(l[k-1:k+1])
            e[(a,b)]=0
ans=0
for v in e.values():
    ans+=v

print(ans)
