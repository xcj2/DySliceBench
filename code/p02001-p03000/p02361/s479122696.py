# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
from heapq import heappop, heappush
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


class Dijkstra:
    """
    shortest_distansce(g): startノードからgoalノードまでの最短距離
    shortest_path(g): startノードからgoalノードまでの最短経路
    """
    def __init__(self, graph, start):
        """
        graph: 隣接リストによるグラフ
        start: 始点のノード番号
        """
        self.g = graph
        self.V = len(graph)

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = [float('inf')] * (self.V)
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = [None] * (self.V)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (0, start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if dist_u > self.dist[u]:
                continue
            for v, weight in self.g[u]:
                alt = self.dist[u] + weight
                if alt < self.dist[v] :
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


def main():
    N,_,start,*edge = map(int, read().split())
    
    E = [[] for _ in range(N)]
    for a, b, w in zip(*[iter(edge)]*3):
        E[a].append((b, w))

    dijkstra = Dijkstra(E, start)
    
    for i in range(N):
        d = dijkstra.shortest_distance(i)
        if d == float('inf'):
            print("INF")
        else:
            print(d)


if __name__ == "__main__":
    main()
