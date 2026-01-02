class Graph:
    class Edge:
        def __init__(self, to, cost):
            """
            :param to:  終点ノード
            :param cost: 辺の重み
            """
            self.to, self.cost = to, cost

    def __init__(self, n, directed=False, decrement=True, edges=[]):
        self.n = n
        self.directed = directed
        self.decrement = decrement
        self.edges2 = []                            # ワーシャルフロイド用
        for x, y, cost in edges:
            self.add_edge(x, y, cost)

    def add_edge(self, x, y, cost):
        if self.decrement:
            x -= 1
            y -= 1
        self.edges2.append((x, y, cost))
        if self.directed == False:
            self.edges2.append((y, x, cost))     # ワーシャルフロイド用

    def warshall_folyd(self, INF=1<<30):
        """
        :param INF: INF = 10**18 にすると、負のコストがある場合に少し面倒になる
        :return: 頂点 i, j 間の距離を行列として返す
        """
        dist = [[INF] * self.n for _ in range(self.n)]

        for i, j, cost in self.edges2:
            dist[i][j] = cost
        for i in range(self.n):
            dist[i][i] = 0  # 自身のところに行くコストは０

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

    def warshall_folyd2(self, INF=1<<30):
        """
        :param INF: INF = 10**18 にすると、負のコストがある場合に少し面倒になる
        :return: 頂点 i, j 間の距離を行列として返す
        """
        dist = [[INF] * self.n for _ in range(self.n)]

        for i, j, cost in self.edges2:
            dist[i][j] = cost
            if dist[i][j] <= L:
                data.append((i, j))
        for i in range(self.n):
            dist[i][i] = 0

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        if dist[i][j] <= L:
                            data.append((i, j))
        return dist

def max2(x,y):
    return x if x > y else y

from itertools import combinations

N, M, L = map(int, input().split())
graph = Graph(N, directed=False, decrement=True)
for _ in range(M):
    x, y, cost = map(int, input().split())
    graph.add_edge(x, y, cost)

data = []
d = graph.warshall_folyd2()

graph2 = Graph(N, directed=False, decrement=False)
for i, j in combinations(range(N), 2):
    if d[i][j] <= L:
        graph2.add_edge(i, j, 1)


d = graph2.warshall_folyd()

for _ in range(int(input())):
    s, t, = map(int, input().split())
    s, t = s-1, t-1
    print(d[s][t]-1 if d[s][t] < 1<<20 else -1)