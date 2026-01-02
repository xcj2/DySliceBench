from collections import deque


class Edge:
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap


# 最大流問題を解く O(|E||V|^2)
class Dinic:
    def __init__(self, num_of_node: int):
        assert num_of_node > 0

        self.graph = [list() for _ in range(num_of_node)]   # グラフの隣接リスト表現
        self.level = [None] * num_of_node      # sからの距離
        self.ite = [None] * num_of_node       # どこまで調べ終わったか

    # fromからtoへ向かう容量capの辺をグラフに追加する
    def add_edge(self, f: int, t: int, cap: int):
        self.graph[f].append(Edge(t, len(self.graph[t]), cap))
        self.graph[t].append(Edge(f, len(self.graph[f]) - 1, 0))

    # sからtへの最大流を求める
    def max_flow(self, s: int, t: int):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0:
                return flow

            self.ite = [0] * len(self.ite)
            while True:
                f = self.dfs(s, t, 10 ** 10)
                if f > 0:
                    flow += f
                else:
                    break

    # sからの最短距離をBFSで計算する
    def bfs(self, s: int):
        self.level = [-1] * len(self.level)
        que = deque()
        que.append(s)
        self.level[s] = 0
        while len(que):
            v = que.popleft()

            for i in range(len(self.graph[v])):
                e = self.graph[v][i]
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1
                    que.append(e.to)

    # 増加パスをDFSで探す
    def dfs(self, v: int, t: int, f: int):
        if v == t:
            return f

        for i in range(0, len(self.graph[v])):
            e = self.graph[v][i]
            if e.cap > 0 and self.level[v] < self.level[e.to]:
                d = self.dfs(e.to, t, min(f, e.cap))
                if d > 0:
                    self.graph[v][i].cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
            self.ite[v] = i
        return 0


def main():
    V, E = map(int, input().split())
    dinic = Dinic(V)
    for _ in range(E):
        u, v, c = map(int, input().split())
        dinic.add_edge(u, v, c)

    print(dinic.max_flow(0, V - 1))


if __name__ == '__main__':
    main()

