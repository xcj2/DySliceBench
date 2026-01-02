from operator import add
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class SegmentTree:
    def __init__(self, N, arr=None, op=None, unit=None):
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
        self.tree[i] += x
        while i > 1:
            i >>= 1
            self.tree[i] = op(self.tree[i << 1], self.tree[i << 1 | 1])

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


if __name__ == "__main__":
    N, Q = map(int, input().split())
    query = tuple(tuple(map(int, input().split())) for _ in range(Q))
    seg = SegmentTree(N, [0]*N, add, 0)

    ans = []
    for f, x, y in query:
        if f:
            ans.append(seg.query(x-1, y))
        else:
            seg.update(x-1, y)
    print(*ans, sep="\n")
