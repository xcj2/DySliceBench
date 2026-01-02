import math
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


class DoublingLCA:
    """
    LCA ダブリング版
    初期化 O(NlogN)、クエリ O(logN)
    """

    def __init__(self, graph, max_v, root):
        """
        :param list of (list of int) graph:
        :param int max_v:
        :param int root:
        """
        self.graph = graph
        self.size = max_v + 1
        self.root = root

        # AtCoder の PyPy 2.4.0 では math.log2 が使えない
        self.MAX_LOG_V = math.floor(math.log(self.size, 2)) + 1
        # depths[v]: v の root からの距離
        self.depths = [-1] * self.size
        # parents[k][v]: 親に 2^k たどった頂点
        self.parents = [[-1] * self.size for _ in range(self.MAX_LOG_V)]

        self._init()

    def _init(self):
        # depths と parents[0] を初期化
        seen = [False] * self.size
        stack = [(self.root, 0, -1)]
        while stack:
            v, d, par = stack.pop()
            self.parents[0][v] = par
            self.depths[v] = d
            seen[v] = True
            for u in self.graph[v]:
                if not seen[u]:
                    stack.append((u, d + 1, v))

        # 各 parents を初期化
        for k in range(self.MAX_LOG_V - 1):
            for v in range(self.size):
                if self.parents[k][v] < 0:
                    # 親がなければ -1
                    self.parents[k + 1][v] = -1
                else:
                    self.parents[k + 1][v] = self.parents[k][self.parents[k][v]]

    def lca(self, u, v):
        """
        :param int u:
        :param int v:
        """
        # 深さを合わせる
        if self.depths[u] > self.depths[v]:
            u, v = v, u
        for k in range(self.MAX_LOG_V):
            if (self.depths[v] - self.depths[u]) >> k & 1:
                v = self.parents[k][v]
        if v == u:
            return v

        # にぶたん
        for k in reversed(range(self.MAX_LOG_V)):
            if self.parents[k][u] != self.parents[k][v]:
                u = self.parents[k][u]
                v = self.parents[k][v]
        return self.parents[0][u]

    def distance(self, u, v):
        """
        u, v 間の距離
        depth[u] + depth[v] - depth[lca] * 2
        :param u:
        :param v:
        :rtype: int
        """
        lca = self.lca(u, v)
        return self.depths[u] + self.depths[v] - self.depths[lca] * 2


# 包除原理つかう

N = int(sys.stdin.buffer.readline())
AB = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N - 1)]
M = int(sys.stdin.buffer.readline())
VU = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(M)]

graph = [[] for _ in range(N)]
edges_i = {}
for i, (a, b) in enumerate(AB):
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    edges_i[a, b] = i
    edges_i[b, a] = i

root = 0
parents = [None] * N
stack = [(root, None)]
while stack:
    v, p = stack.pop()
    parents[v] = p
    for u in graph[v]:
        if u == p:
            continue
        stack.append((u, v))

lca = DoublingLCA(graph=graph, max_v=N - 1, root=root)
constraints = [0] * M
# 制約ごとにどの辺を使うかを持つ
for i, (v, u) in enumerate(VU):
    v -= 1
    u -= 1
    ancestor = lca.lca(v, u)
    while v != ancestor:
        constraints[i] |= 1 << edges_i[v, parents[v]]
        v = parents[v]
    while u != ancestor:
        constraints[i] |= 1 << edges_i[u, parents[u]]
        u = parents[u]


# for c in constraints:
#     print(np.binary_repr(c, 10))


def count(edges_bin):
    cnt = 0
    while edges_bin > 0:
        cnt += edges_bin & 1
        edges_bin >>= 1
    return pow(2, N - 1 - cnt)


# 余事象を数える
# 制約をいくつか選んだときに、1つ以上の制約を満たさない場合の数
# 1つの制約を満たさない数は、2^(制約と関係ない辺の数) == 2^((N - 1) - 使う辺の数)
ans = 0
for choice in range(1, 1 << M):
    cnt = 0
    edges = 0
    for i in range(choice.bit_length()):
        if choice >> i & 1:
            cnt += 1
            edges |= constraints[i]
    ans += count(edges) * (-1) ** (cnt - 1)
print(2 ** (N - 1) - ans)
