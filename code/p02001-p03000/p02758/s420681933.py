import sys
import bisect
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
inf = 10**18
mod = 998244353


class SegmentTree:
    def __init__(self, N, arr=None, op=None, unit=None):
        """
        INPUT
        N: 配列のサイズ
        segment tree: 1-indexedで構築
        original array: 0-indexed
                 1
           2           3
         4    5     6     7
        8 9 10 11 12 13 14 15
        ---------------------
        0 1 2  3  4  5  6  7
        """
        self.N = N
        self.unit = unit
        self.op = op
        self.tree = [unit] * (2 * N + 1)
        if arr is not None:
            self._build(arr)

    def _build(self, arr):
        op = self.op
        N = self.N
        for i, a in enumerate(arr, N):
            self.tree[i] = a
        for i in reversed(range(1, N)):
            self.tree[i] = op(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, i, x):
        """
        arr[i]の値をxに変更する
        i: 0-indexed
        """
        i += self.N
        op = self.op
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = op(self.tree[i << 1], self.tree[i << 1 | 1])

    def val(self, i):
        return self.tree[i + self.N]

    def query(self, L, R):
        """
        L,R: 0-indexed
        半開区間[L,R)の累積演算した値を返す
        """
        op = self.op
        res = self.unit
        L += self.N
        R += self.N
        while L < R:
            if L & 1:
                res = op(res, self.tree[L])
                L += 1
            if R & 1:
                R -= 1
                res = op(res, self.tree[R])
            L >>= 1
            R >>= 1
        return res


N = int(input())
XD = list(tuple(map(int, input().split())) for _ in range(N))
XD.sort()
X, D = zip(*XD)
X += (inf, )


seg = SegmentTree(N+1, None, max, 0)
for L in reversed(range(N)):
    R = bisect.bisect_left(X, X[L] + D[L])
    p = seg.query(L, R)
    seg.update(L, max(L, p))

dp = [0] * (N + 1)
dp[-1] = 1
for i in reversed(range(N)):
    p = seg.val(i)
    dp[i] = (dp[i + 1] + dp[p + 1]) % mod

print(dp[0])