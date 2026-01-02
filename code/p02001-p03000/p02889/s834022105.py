from math import isinf


class WarshallFloyd(object):

    def __init__(self, adj):
        """
        ワーシャル・フロイド法によって全頂点間の最短距離を O(|V|^3) で計算する。

        :param adj: 隣接行列 adj[i][j] でi番目の頂点からj番目の頂点へのコストを示す パスがなければINF
        """
        self._dist = adj  # 各頂点間の最短距離 初期値として隣接行列をそのまま用い、[i, i]要素を0に初期化する
        for i in range(len(adj)):
            self._dist[i][i] = 0

        self._solve()

    def _solve(self):
        v_len = len(self._dist)
        for i in range(v_len):  # 経由する頂点
            for j in range(v_len):  # 開始頂点
                for k in range(v_len):  # 終端
                    self._dist[j][k] = min(self._dist[j][k], self._dist[j][i] + self._dist[i][k])

    def distance(self, start, goal):
        return self._dist[start][goal]

    def path(self, start, goal):
        pass


N, M, L = map(int, input().split())
adj = [[float('inf') for _ in range(N)] for _ in range(N)]
for A, B, C in [tuple(map(int, input().split())) for _ in range(M)]:
    adj[A - 1][B - 1] = C
    adj[B - 1][A - 1] = C

wf = WarshallFloyd(adj)

adj2 = [[float('inf') for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if wf.distance(i, j) <= L:
            adj2[i][j] = 1
wf2 = WarshallFloyd(adj2)

Q = int(input())
for s, t in [tuple(map(int, input().split())) for _ in range(Q)]:
    ans = wf2.distance(s - 1, t - 1) - 1
    if isinf(ans):
        print(-1)
    else:
        print(ans)
