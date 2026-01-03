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

    def add_edge(self, src, dst, weight=1):  # デフォルトの距離は1
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    """
    ダイクストラ法 (二分ヒープ) による最短経路探索
    計算量: O((E+V)logV)
    """

    def __init__(self, graph, start):  # graph: Graphオブジェクト, start: 始点のIndex
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

        # そのノードまでの最短経路を定義した時、どのノードから来たのかを記録する
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))  # そのノードまでの仮の最短距離, ノードのIndex
        # 本当の最短距離はself.distに格納する
        while self.Q:
            # 距離が最小であるものをキューから取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:  # 仮の距離より短い距離が正式に求まっているならスルー
                continue
            for v, weight in self.g[u]:  # 対象のノードに隣接しているノードに対して操作を行う, 始点はu
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))  # 更新された仮の距離, ノード

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
        while node is not None:  # startノードはprevを持たないからこの条件でよい
            path.append(node)
            node = self.prev[node]
        return path[::-1]  # 逆順にして返す


N, M = map(int, input().split())
g = Graph()
visited_edges = {}
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g.add_edge(a, b, c)
    g.add_edge(b, a, c)
    visited_edges[(a, b)] = False
    visited_edges[(b, a)] = False

for i in range(N):  # 始点
    shortest = Dijkstra(g, i)
    for j in range(i+1, N):  # 終点
        paths = shortest.shortest_path(j)
        for k in range(len(paths)-1):
            visited_edges[(paths[k], paths[k+1])] = True
            visited_edges[(paths[k+1], paths[k])] = True
print(M - sum(visited_edges.values())//2)
