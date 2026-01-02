# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=ja
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


class BellmanFord:
    """
    shortest_distance(goal): startノードからgoalノードまでの最短距離
    shortest_path(goal): startノードからgoalノードまでの最短経路
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
        始点から頂点goalまでの最短距離をを返す 
        """
        d = [float('inf')] * self.V
        d[self.start] = 0

        # 最短経路での1つ前のノードを保持するリスト
        self.prev = [None] * self.V

        loop_counter = 0
        while True:
            update = False
            # start, end, cost
            for s, e, c  in self.edges:
                if d[s] != float('inf') and d[e] > d[s] + c:
                    d[e] = d[s] + c
                    self.prev[e] = s
                    update = True
            
            loop_counter += 1
            if loop_counter == self.V and update:
                d[self.start] = float('inf')
                break

            if not update:
                break
        
        return d

    def shortest_path(self, goal):
        """
        始点から頂点goalまでの最短経路をを返す 
        """
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


def main():
    V, _, r, *edge = map(int, read().split())
    
    Edges = []
    for a, b, w in zip(*[iter(edge)]*3):
        Edges.append((a, b, w))

    bf = BellmanFord(V, Edges, r)
        
    dist = bf.shortest_distance()
    if dist[r] == float('inf'):
        print("NEGATIVE CYCLE")
    else:
        for d in dist:
            print(d if d < float('inf') else "INF")


if __name__ == "__main__":
    main()
