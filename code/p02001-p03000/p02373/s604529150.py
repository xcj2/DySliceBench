import operator
import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
for i in range(N):
    _, *c = list(map(int, sys.stdin.readline().split()))
    graph[i] = c
Q = int(sys.stdin.readline())
UV = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]


class SegmentTree:
    # http://tsutaj.hatenablog.com/entry/2017/03/29/204841
    def __init__(self, size, fn=operator.add, default=None, initial_values=None):
        """
        :param int size:
        :param callable fn: 区間に適用する関数。引数を 2 つ取る。min, max, operator.xor など
        :param default:
        :param list initial_values:
        """
        default = default or 0

        # size 以上である最小の 2 冪
        n = 1
        while n < size:
            n *= 2
        self._size = n
        self._fn = fn

        self._tree = [default] * (self._size * 2 - 1)
        if initial_values:
            i = self._size - 1
            for v in initial_values:
                self._tree[i] = v
                i += 1
            i = self._size - 2
            while i >= 0:
                self._tree[i] = self._fn(self._tree[i * 2 + 1], self._tree[i * 2 + 2])
                i -= 1

    def set(self, i, value):
        """
        i 番目に value を設定
        :param int i:
        :param value:
        :return:
        """
        x = self._size - 1 + i
        self._tree[x] = value

        while x > 0:
            x = (x - 1) // 2
            self._tree[x] = self._fn(self._tree[x * 2 + 1], self._tree[x * 2 + 2])

    def add(self, i, value):
        """
        もとの i 番目と value に fn を適用したものを i 番目に設定
        :param int i:
        :param value:
        :return:
        """
        x = self._size - 1 + i
        self.set(i, self._fn(self._tree[x], value))

    def get(self, from_i, to_i, k=0, L=None, r=None):
        """
        [from_i, to_i) に fn を適用した結果を返す
        :param int from_i:
        :param int to_i:
        :param int k: self._tree[k] が、[L, r) に fn を適用した結果を持つ
        :param int L:
        :param int r:
        :return:
        """
        L = 0 if L is None else L
        r = self._size if r is None else r

        if from_i <= L and r <= to_i:
            return self._tree[k]

        if to_i <= L or r <= from_i:
            return None

        ret_L = self.get(from_i, to_i, k * 2 + 1, L, (L + r) // 2)
        ret_r = self.get(from_i, to_i, k * 2 + 2, (L + r) // 2, r)
        if ret_L is None:
            return ret_r
        if ret_r is None:
            return ret_L
        return self._fn(ret_L, ret_r)

    def __len__(self):
        return self._size


def tree_eulerian_trail(graph, root=0):
    """
    木のオイラー路; オイラーツアー
    :param list of (list of int) graph:
    :param int root:
    :return: (trails, depths)
    :rtype: (list of int, list of int)
    """
    # 頂点の履歴
    trails = []
    # 深さの履歴
    depths = []
    # Overflow 回避のためループで
    stack = [(root, 0, True)]
    while stack:
        v, d, forward = stack.pop()
        trails.append(v)
        depths.append(d)
        if not forward:
            continue
        for u in graph[v]:
            stack.append((v, d, False))
            stack.append((u, d + 1, True))
    return trails, depths


trails, depths = tree_eulerian_trail(graph, 0)
# ids[v]: trails が v となる trails / depths のインデックス
ids = [0] * N
for i, v in enumerate(trails):
    ids[v] = i

# depths[v] から depths[u] までの最小値が LCA
st = SegmentTree(size=len(depths), fn=min, default=(IINF, -1), initial_values=list(zip(depths, trails)))

# RmQ
for u, v in UV:
    iu, iv = ids[u], ids[v]
    if iu > iv:
        iu, iv = iv, iu
    _, lca = st.get(iu, iv + 1)
    print(lca)

