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


n,m,s = map(int, input().split())
uvab = [list(map(int, input().split())) for i in range(m)]
cd = [list(map(int, input().split())) for i in range(n)]

G = Graph()
for u,v,a,b in uvab:
    u-=1
    v-=1
    u*=2501
    v*=2501
    for i in range(2500,a-1,-1):
        G.add_edge(u+i,v+i-a,b)
        G.add_edge(v+i,u+i-a,b)
for i,(c,d) in enumerate(cd):
    i*=2501
    for j in range(2501-c):
        G.add_edge(i+j,i+j+c,d)

s = min(s,2500)
dist = Dijkstra(G, s)
for i in range(1,n):
    ans = 10 ** 18
    for j in range(2501):
        goal = i * 2501 + j
        D = dist.shortest_distance(goal)
        ans = min(ans, D)
    print(ans)
