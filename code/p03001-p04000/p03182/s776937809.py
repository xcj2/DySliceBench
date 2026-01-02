from operator import add
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)


class LazySegmetTree:
    def __init__(self, size, op_data, u_data, op_lazy, u_lazy, op_merge):
        """
        size: 元の配列の長さ
        op_data, u_data: クエリ関数、単位元
        op_lazy, u_lazy: 遅延作用の関数、単位元
        op_merge: dataとlazyとの演算
        """
        self.N = size
        self.op_data = op_data
        self.op_lazy = op_lazy
        self.op_merge = op_merge
        self.u_data = u_data
        self.u_lazy = u_lazy
        #self.data = [u_data] * (2 * self.N)
        self.data = [0] * (2 * self.N)
        self.lazy = [u_lazy] * (2 * self.N)

    def initialize(self, arr):
        op = self.op_data
        for i, a in enumerate(arr, self.N):
            self.data[i] = a
        for i in reversed(range(1, self.N)):
            self.data[i] = op(self.data[i << 1], self.data[i << 1 | 1])

    def _propagate_top_down(self, L):
        op = self.op_lazy
        merge = self.op_merge
        unit = self.u_lazy
        for i in reversed(range(1, L.bit_length())):
            i = L >> i
            v = self.lazy[i]
            if v == unit:
                continue
            self.data[i] = merge(self.data[i], v)
            self.lazy[i << 1] = op(self.lazy[i << 1], v)
            self.lazy[i << 1 | 1] = op(self.lazy[i << 1 | 1], v)
            self.lazy[i] = unit

    def _propagate_bottom_up(self, i):
        merge = self.op_merge
        op = self.op_data
        while i > 1:
            i >>= 1
            self.data[i] = op(merge(self.data[i << 1], self.lazy[i << 1]),
                              merge(self.data[i << 1 | 1], self.lazy[i << 1 | 1]))

    def fold(self, L, R):
        res = self.u_data
        op = self.op_data
        merge = self.op_merge
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self._propagate_top_down(L0)
        self._propagate_top_down(R0)
        while L < R:
            if L & 1:
                res = op(res, merge(self.data[L], self.lazy[L]))
                L += 1
            if R & 1:
                R -= 1
                res = op(res, merge(self.data[R], self.lazy[R]))
            L >>= 1
            R >>= 1
        return res

    def update(self, i, val):  # 未調整
        i += self.N
        i0 = i // (i & -i)
        self._propagate_top_down(i0)
        self.data[i] = self.op_merge(self.data[i], self.lazy[i])
        self.data[i] = self.op_data(val, self.data[i])
        self.lazy[i] = self.u_lazy
        self._propagate_bottom_up(i0)

    def range_update(self, L, R, val):
        op = self.op_lazy
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self._propagate_top_down(L0)
        self._propagate_top_down(R0)
        while L < R:
            if L & 1:
                self.lazy[L] = op(val, self.lazy[L])
                L += 1
            if R & 1:
                R -= 1
                self.lazy[R] = op(val, self.lazy[R])
            L >>= 1
            R >>= 1
        self._propagate_bottom_up(L0)
        self._propagate_bottom_up(R0)


def main():
    N, M = map(int, input().split())
    LRA = list(tuple(map(int, input().split())) for _ in range(M))
    LRA.sort(key=lambda x: x[1])

    op_data = max
    unit_data = -10 ** 18
    op_lazy = add
    unit_lazy = 0
    op_merge = add
    seg = LazySegmetTree(N + 1, op_data, unit_data,
                         op_lazy, unit_lazy, op_merge)

    p = 0
    for i in range(N):
        val = seg.fold(0, i + 1)
        seg.update(i + 1, val)
        while p < M and LRA[p][1] <= i + 1:
            l, r, a = LRA[p]
            p += 1
            seg.range_update(l, r + 1, a)

    print(seg.fold(0, N + 1))


if __name__ == "__main__":
    main()