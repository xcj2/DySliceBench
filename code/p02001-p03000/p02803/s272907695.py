H, W = map(int, input().split())
N = H * W
S = [input() for _ in range(H)]


def idx(i, j):
    return i * W + j


adj = [[float('inf')] * N for _ in range(N)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        index = idx(i, j)
        if i > 0 and S[i - 1][j] == '.':
            adj[index][idx(i - 1, j)] = 1
            adj[idx(i - 1, j)][index] = 1
        if j < W - 1 and S[i][j + 1] == '.':
            adj[index][idx(i, j + 1)] = 1
            adj[idx(i, j + 1)][index] = 1
        if i < H - 1 and S[i + 1][j] == '.':
            adj[index][idx(i + 1, j)] = 1
            adj[idx(i + 1, j)][index] = 1
        if j > 0 and S[i][j - 1] == '.':
            adj[index][idx(i, j - 1)] = 1
            adj[idx(i, j - 1)][index] = 1

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


from math import isinf

wf = WarshallFloyd(adj)
ans = 0
for r in wf._dist:
    m = max(filter(lambda x: not isinf(x), r))
    ans = max(ans, m)
print(ans)