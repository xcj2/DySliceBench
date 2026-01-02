from itertools import permutations


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


N, M, R = map(int, input().split())
r = list(map(int, input().split()))
adj = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A][B] = C
    adj[B][A] = C

wf = WarshallFloyd(adj)

ans = float('inf')
tours = list(map(list, permutations(r, R)))
for tour in tours:
    cost = 0
    for i in range(1, len(tour)):
        cost += wf.distance(tour[i - 1], tour[i])
    ans = min(ans, cost)
print(ans)
