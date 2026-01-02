from collections import defaultdict
from heapq import heappop, heappush
h, w = map(int, input().split())
d = []
for i in range(h):
    d.append(input())
# [d1, d2, d3, ..., dN]
s = [str(m) for m in d]
#移動ベクトル
dd = ((0, -1), (-1, 0), (0, 1), (1, 0))
dist = []
dotcount = 0
sharpcount = 0
for j in range(h):
    for i in range(w):
        if s[j][i] == ".":
            dotcount += 1
            for dx, dy in dd:  # 下、左、上、右の四方向から生物種が流れこむ、もしくは流れ出る（濃度の違いによって決定される、濃度が高いほうから低いほうに流れる）
                nx = i + dx
                ny = j + dy
                if 0 <= nx < w and 0 <= ny < h:  # L*Lの幅に収まっているときのみ
                    if s[ny][nx] == ".":
                        dist.append([i + j * w, nx + ny * w, 1])
        else:
            sharpcount += 1

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
# (src, dst, weight)
inputs = dist

g = Graph()
for src, dst, weight in inputs:
    g.add_edge(src, dst, weight)
    g.add_edge(dst, src, weight)

d = Dijkstra(g, h * w - 1)
sp = format(d.shortest_distance(0))
#print('最短経路: {}'.format(d.shortest_path(1)))
#print('最短距離: {}'.format(d.shortest_distance(1)))
if sp != "inf":
    needcount = int(sp) + 1
    ans = dotcount - needcount
else:
    ans = -1

print(ans)