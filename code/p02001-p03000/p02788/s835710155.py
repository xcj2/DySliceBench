import sys
sys.setrecursionlimit(2147483647)
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()

class SegmentTree(object):
    def __init__(self, A, dot, unit):
        n = 1 << (len(A) - 1).bit_length()
        tree = [unit] * (2 * n)
        for i, v in enumerate(A):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n = n
        self._tree = tree
        self._dot = dot
        self._unit = unit

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def update(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])

    def add(self, i, v):
        self.update(i, self[i] + v)

    def sum(self, l, r):
        l += self._n
        r += self._n
        l_val = r_val = self._unit
        while l < r:
            if l & 1:
                l_val = self._dot(l_val, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self._dot(self._tree[r], r_val)
            l >>= 1
            r >>= 1
        return self._dot(l_val, r_val)

from bisect import bisect_right
from operator import add
def resolve():
    n, d, a = map(int, input().split())
    X = [None] * n
    XH = [None] * n
    for i in range(n):
        x, h = map(int, input().split())
        X[i] = x
        XH[i] = x, (h - 1) // a + 1

    X.sort()
    XH.sort()

    tree = SegmentTree([0] * (n + 1), add, 0)
    res = 0
    for i in range(n):
        x, h = XH[i]
        damage = tree.sum(0, i + 1)
        if h < damage:
            continue
        res += h - damage
        tree.add(i, h - damage)
        tree.add(bisect_right(X, x + 2 * d), - h + damage)

    print(res)
resolve()