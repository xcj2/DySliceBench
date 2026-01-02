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


N, M, s, t = map(int, input().split())  # N個の町, M本の電車, 始点s, 終点t
s -= 1
t -= 1
# 最後は終点でしかスヌークにしか変えられなくなる
graph = Graph()
reverse_graph = Graph()
for _ in range(M):
    u, v, a, b = map(int, input().split())  # 始点, 終点, 円, スヌーク
    u -= 1
    v -= 1
    graph.add_edge(u, v, a)
    graph.add_edge(v, u, a)
    reverse_graph.add_edge(u, v, b)
    reverse_graph.add_edge(v, u, b)


shortest_from_start = Dijkstra(graph, s)
shortest_from_goal = Dijkstra(reverse_graph, t)


# 逆から考える, どんどん選択肢が増えるようにする, 最初は一番厳しい制約
price = shortest_from_start.shortest_distance(N-1)+shortest_from_goal.shortest_distance(N-1)
ans = [price]  # 最後にreverseする

# 最初に、どこでも換金できないパターンの値を求めて、それから、換金できる場所を増やしていってそこで換金する場合に値が変わるかどうかを確かめていく
for i in reversed(range(N-1)):  # iが換金する場所
    ans.append(min(ans[-1], shortest_from_start.shortest_distance(i)+shortest_from_goal.shortest_distance(i)))
ans.reverse()

for a in ans:
    print(10**15 - a)
