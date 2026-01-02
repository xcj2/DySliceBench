import operator
import os
import sys
from functools import reduce

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


class LazySegmentTree:
    # http://codeforces.com/blog/entry/18051
    def __init__(self, values, fn=operator.add):
        """
        :param list values:
        :param callable fn:
        """
        # 単位元
        self._id = 0
        self._size = len(values)
        self._fn = fn

        tree = [self._id] * self._size * 2
        tree[self._size:] = values[:]
        for i in reversed(range(1, self._size)):
            tree[i] = fn(tree[i << 1], tree[i << 1 | 1])
        self._tree = tree
        self._delay = [self._id] * self._size * 2

    def _add(self, k, value):
        if k < self._size:
            self._delay[k] = self._delay[k] + value
        else:
            self._tree[k] = self._tree[k] + value

    def add(self, l, r, value):
        """
        :param int l:
        :param int r:
        :param value:
        """
        l += self._size
        r += self._size
        l0, r0 = l, r
        while l < r:
            if l & 1:
                # 右側の子
                self._add(l, value)
                l += 1
            if r & 1:
                # 左側の子
                r -= 1
                self._add(r, value)
            l >>= 1
            r >>= 1
        self._update(l0)
        self._update(r0)

    def _update(self, p):
        """
        self._tree[p] の親たちを最新化する
        :param int p:
        """
        p >>= 1
        while p > 0:
            self._tree[p] = self._fn(
                self._tree[p << 1] + self._delay[p << 1],
                self._tree[p << 1 | 1] + self._delay[p << 1 | 1]
            )
            p >>= 1

    def _eval(self, p):
        """
        self._tree[p] に遅延配列から値を移す
        :param int p:
        """
        # root から葉に向かって遅延配列を移していく
        for h in reversed(range(1, p.bit_length())):
            k = p >> h
            self._tree[k] = self._tree[k] + self._delay[k]
            self._add(k << 1, self._delay[k])
            self._add(k << 1 | 1, self._delay[k])
            self._delay[k] = self._id

    def get(self, l, r=None):
        """
        :param int l:
        :param int|None r:
        """
        if r is None:
            self._eval(self._size + l)
            return self._tree[self._size + l]
        ret_l = []
        ret_r = []
        l += self._size
        r += self._size
        self._eval(l)
        self._eval(r)
        while l < r:
            if l & 1:
                ret_l.append(self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret_r.append(self._tree[r])
            l >>= 1
            r >>= 1
        return reduce(self._fn, ret_l + ret_r)


N, D, A = list(map(int, sys.stdin.buffer.readline().split()))
XH = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

XH.sort()
X = []
H = []
for x, h in XH:
    X.append(x)
    H.append(h)

lr = []
r = 0
for l in range(N):
    while r < N and X[r] <= X[l] + D * 2:
        r += 1
    lr.append((l, r))

st = LazySegmentTree(values=H + [0], fn=operator.add)
ans = 0
for l, r in lr:
    h = st.get(l, l + 1)
    if h > 0:
        cnt = (h + A - 1) // A
        st.add(l, r, -cnt * A)
        ans += cnt
print(ans)
