# ABC068c
import collections
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
INF = 10**12


class Edge:  # 通常の辺
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost


class Dijkstra:  # ダイクストラ法 O(E * logV)
    def __init__(self, n):
        self.n = n
        self.dist = [INF for _ in range(n)]
        self.edges = [list() for _ in range(n)]
        self.q = collections.deque()

    def calcShortest(self, start):
        self.q.append((start, 0))
        while(len(self.q) != 0):
            v, cost = self.q.popleft()
            if cost > 2:
                continue
            if self.dist[v] <= cost:
                continue
            self.dist[v] = cost
            for edge in self.edges[v]:
                self.q.append((edge.to, cost+edge.cost))

    def addEdge(self, st, gl, cost):
        self.edges[st].append(Edge(gl, cost))


v = Dijkstra(n)
for _ in range(m):
    a, b = map(int, input().split())
    v.addEdge(a-1, b-1, 1)
    v.addEdge(b-1, a-1, 1)

v.calcShortest(0)
if v.dist[n-1] <= 2:
    print('POSSIBLE')
    exit(0)
print('IMPOSSIBLE')
