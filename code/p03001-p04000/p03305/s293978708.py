from collections import defaultdict
from heapq import heappop, heappush, heapify


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


def main():
    n, m, s, t = map(int, input().split())
    trains = [list(map(int, input().split())) for i in range(m)]

    g_yen = Graph()
    g_snuuk = Graph()

    for train in trains:
        u, v, a, b = train
        g_yen.add_edge(u, v, a)
        g_yen.add_edge(v, u, a)
        g_snuuk.add_edge(u, v, b)
        g_snuuk.add_edge(v, u, b)

    d_yen = Dijkstra(g_yen, s)
    d_snuuk = Dijkstra(g_snuuk, t)

    cost_sum = []
    for i in range(1, n+1):
        cost_sum.append([d_yen.dist[i] + d_snuuk.dist[i], i])

    heapify(cost_sum)
    c, l = heappop(cost_sum)
    for i in range(n):
        while l<=i:
            c, l = heappop(cost_sum)
        print(10**15 - c)


if __name__ == '__main__':
     main()
    




