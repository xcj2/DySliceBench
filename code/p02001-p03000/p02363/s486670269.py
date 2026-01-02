# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja
# Johnsonのアルゴリズム
# Bellman-Ford法で負辺を消去した後、
# 各頂点からダイクストラを行う
from heapq import heappop, heappush
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


class BellmanFord:
    """
    shortest_distance(): startノードから各ノードまでの最短距離
    include_negative_cycle(): 負閉路の存在確認
    """
    def __init__(self, V, edges, start):
        """
        V : 頂点数
        edges: (辺の始点,辺の終点,辺のコスト)を要素とする辺のリスト
        start: 始点のノード番号
        """
        self.V = V
        self.edges = edges
        self.start = start

    def include_negative_cycle(self):
        """
        負閉路の存在確認
        Returns: True or False
        """
        d = [0] * self.V
        for i in range(self.V):
            # start, end, cost
            for s, e, c in self.edges:
                if d[e] > d[s] + c:
                    d[e] = d[s] + c
                    # V回目にも更新があるなら負の閉路が存在する
                    if i == self.V-1:
                        return True
        return False
                    
    def shortest_distance(self):
        """ 
        始点から各頂点までの最短距離をを返す
        負閉路に到達可能ならば d[start] = INF
        """
        d = [float('inf')] * self.V
        d[self.start] = 0

        loop_counter = 0
        while True:
            update = False
            # start, end, cost
            for s, e, c  in self.edges:
                if d[s] != float('inf') and d[e] > d[s] + c:
                    d[e] = d[s] + c
                    update = True
            
            # 負閉路の到達しないならばループは高々V-1回
            # ループ回数がV回の時点で更新があるならば負閉路に到達してしまう
            loop_counter += 1
            if loop_counter == self.V and update:
                d[self.start] = float('inf')
                break

            if not update:
                break
        
        return d


class Dijkstra:
    """
    shortest_distance(): startノードから各ノードまでの最短距離
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
        self.dist = [float('inf')] * self.V
        self.dist[start] = 0

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
                    heappush(self.Q, (alt, v))

    def shortest_distance(self):
        return self.dist


def main():
    V,E,*std = map(int, read().split())

    Edges = []
    for i in range(V):
        Edges.append((V, i, 0))

    for s,t,d in zip(*[iter(std)]*3):
        Edges.append((s, t, d))
    
    # 超頂点からBellman-Ford O(VE)
    bf = BellmanFord(V+1, Edges, V)
    h = bf.shortest_distance()
    
    if float('inf') in h:
        print("NEGATIVE CYCLE")
    else:
        Graph = [[] * V for _ in range(V)]
        for s, t, d in Edges:
            if s == V:
                continue
            else:
                Graph[s].append((t, d + h[s] - h[t]))
        
        ans = []
        # 各頂点からDijkstra O(VElogV)
        for i in range(V):
            d = Dijkstra(Graph, i)
            ans.append(d.shortest_distance())
    
        # 重みを元に戻す O(V^2)
        for i, line in enumerate(ans):
            h_i = h[i]
            for j, n in enumerate(line):
                if n == float('inf'):
                    line[j] = "INF"
                else:
                    line[j] -= h_i - h[j]
            tmp = " ".join(map(str, line))
            print(tmp)


if __name__ == "__main__":
    main()
