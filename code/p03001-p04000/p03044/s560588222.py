import collections
import heapq

def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

class Dijkstra():
    
    def __init__(self):  self.e = collections.defaultdict(list)

    def add(self, u, v, d, directed = False):
        self.e[u].append([v, d])
        self.e[v].append([u, d]) # 有向グラフの場合、コメントアウト

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):

        d = collections.defaultdict(lambda: float('inf'))
        prev = collections.defaultdict(lambda: None)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while q:
        
            k, u = heapq.heappop(q)
            if v[u]:  continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:  continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d, prev

    def getDijkstraShortestPath(self, start, goal):
        _, prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]

graph = Dijkstra()
N = cin()
for i in range(N - 1): 
    in_ = cin()
    graph.add(in_[0] - 1, in_[1] - 1, in_[2])
min_w, prev = graph.Dijkstra_search(0)
ans = [0 for _ in range(N)]
for i in range(N):  print(min_w[i] % 2)