#!/usr/bin/env python3
import sys
INF = float("inf")


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.V = list(range(N))
        self.E = [[] for _ in range(N)]

    def add_edge(self, edge):
        """辺を加える。edgeは(始点, 終点、重み)からなるリスト
        重みがなければ、重み1とする。
        """
        if len(edge) == 2:
            edge.append(1)
        elif len(edge) != 3:
            print("error in add_edge")
            pass

        s, t, w = edge
        self.E[s].append([t, w])
        self.E[t].append([s, w])  # 無向グラフを仮定。逆向きにも辺を張る

        pass

    def remove_edge(self, edge):
        if len(edge) == 2:
            edge.append(1)
        elif len(edge) != 3:
            print("error in add_edge")
            pass

        s, t, w = edge
        for tt, ww in self.E[s]:
            if tt == t:
                break
        if tt == t:
            self.E[s].remove([t, ww])
            self.E[t].remove([s, ww])
        pass


def Warshall_Floyd(g: Graph):
    """ワーシャルフロイド法により、全節点対の最短距離を求める。O(V^3)
    https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E2%80%93%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95
    """
    N = g.N
    dist = [[INF]*N for _ in range(N)]
    for from_, toweights in enumerate(g.E):
        for to_, w in toweights:
            dist[from_][to_] = w

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def solve(N: int, A: "List[List[int]]"):

    g = Graph(N)
    for i in range(N):
        for j in range(i+1, N):
            g.add_edge([i, j, A[i][j]])

    B = Warshall_Floyd(g)

    counter = 0
    for i in range(N):
        for j in range(i+1, N):
            if B[i][j] < A[i][j]:
                print(-1)
                return

            flag = True
            for k in range(N):
                if B[i][j] == B[i][k]+B[k][j]:
                    flag = False
            if flag == True:
                counter += B[i][j]
    print(counter)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)]
         for _ in range(N)]  # type: "List[List[int]]"

    solve(N, A)


if __name__ == '__main__':
    main()
