import bisect
import operator
import os
import sys
from functools import reduce


class SegmentTree:
    # http://codeforces.com/blog/entry/18051
    def __init__(self, values, op=operator.add):
        """
        :param list values:
        :param callable op: 結合律を満たす二項演算
        """
        self._size = len(values)
        self._op = op
        tree = [None] * self._size * 2
        tree[self._size:] = values[:]
        for i in reversed(range(1, self._size)):
            tree[i] = self._op(tree[i << 1], tree[i << 1 | 1])
        self._tree = tree

    def set(self, i, value):
        """
        values[i] = value
        :param int i:
        :param value:
        """
        i += self._size
        self._tree[i] = value
        i >>= 1
        while i > 0:
            self._tree[i] = self._op(self._tree[i << 1], self._tree[i << 1 | 1])
            i >>= 1

    def add(self, i, value):
        """
        values[i] = values[i]・value
        :param int i:
        :param value:
        """
        new_value = self._op(self._tree[self._size + i], value)
        self.set(i, new_value)

    def get(self, l, r=None):
        """
        [l, r) に op を順番に適用した値
        :param int l:
        :param int|None r:
        """
        if r is None:
            return self._tree[self._size + l]
        ret_l = []
        ret_r = []
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                ret_l.append(self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret_r.append(self._tree[r])
            l >>= 1
            r >>= 1
        return reduce(self._op, ret_l + ret_r)

    def __len__(self):
        return self._size


if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 998244353

N = int(sys.stdin.buffer.readline())
XD = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

XD.sort()
X = [x for x, d in XD]
D = [d for x, d in XD]

# R[i]: i 番目のロボットがどこまで行くか
st = SegmentTree(list(range(N)), op=max)
for i, (x, d) in reversed(list(enumerate(XD))):
    ri = bisect.bisect_left(X, x + d) - 1
    st.set(i, st.get(i, ri + 1))
R = [st.get(i) for i in range(N)]

# dp[i]: ロボット i からロボット N - 1 までを使うときの組み合わせの数
dp = [0] * (N + 1)
dp[-1] = 1
for i, r in reversed(list(enumerate(R))):
    # 使わない場合
    dp[i] += dp[i + 1]
    # 使う場合
    dp[i] += dp[r + 1]
    dp[i] %= MOD
# print(dp)
print(dp[0])
