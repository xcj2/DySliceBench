from collections import defaultdict
from heapq import heappop, heappush

class Graph(object):
    """
    隣接リストによる有向グラフ
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    """
    ダイクストラ法（二分ヒープ）による最短経路探索
    計算量: O((E+V)logV)
    """

    def __init__(self, graph, start):
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
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
        """
        startノードからgoalノードまでの最短距離
        """
        return self.dist[goal]

    def shortest_path(self, goal):
        """
        startノードからgoalノードまでの最短経路
        """
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]

g = Graph()
N,M = list(map(int, input().split()))
INF = 10**9+7
A = [[INF if i!=j else 0 for i in range(N)] for j in range(N)]
S=[]
E=[]
W=[]

for i in range(M):
    s,e,w=list(map(int,input().split()))
    g.add_edge(s-1, e-1, w)
    g.add_edge(e-1, s-1, w)
    S.append(s-1)
    E.append(e-1)
    W.append(w)

for i in range(N):
    d = Dijkstra(g, i)
    for j in range(i+1,N):
        dist = d.shortest_distance(j)
        A[i][j] = dist
        A[j][i] = dist
        
ans=M
for i in range(M):
    shortest = False
    for j in range(N):
        if A[j][S[i]] + W[i] == A[j][E[i]]:
            shortest = True
    if shortest:
        ans-=1

print(ans)