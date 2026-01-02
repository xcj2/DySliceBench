from collections import defaultdict
from heapq import heappop, heappush
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


class Graph:
    """
    隣接リストによる無向グラフ
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))
        self.graph[dst].append((src, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra:
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
                    heappush(self.Q, (alt, v))

    def shortest_distance(self):
        """
        startノードから各ノードまでの最短距離
        """
        return self.dist


def main():
    N,x,y = map(int, readline().split())

    # グラフの構築
    E = Graph()
    for i in range(1,N):
        if i == x:
            E.add_edge(x, y)
        E.add_edge(i, i+1)
    
    # 各頂点についてダイクストラ
    count = [0]*N
    for i in range(1,N):
        D = Dijkstra(E, i)
        dist = D.shortest_distance()
        for j in range(i+1,N+1):
            k = dist[j]
            count[k] += 1

    for k in range(1,N):
        print(count[k])


if __name__ == "__main__":
    main()
