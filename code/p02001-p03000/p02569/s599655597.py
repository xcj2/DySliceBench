from operator import xor
from typing import Callable, List, TypeVar

S = TypeVar("S")  # モノイドの型
F = TypeVar("F")  # 写像の型


class LazySegmentTree:
    """
    Lazy Segment Tree from https://atcoder.jp/contests/practice2/submissions/16775176
    References:
        https://tumoiyorozu.github.io/single-file-ac-library/document_ja/lazysegtree.html
        https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp
    """

    __slots__ = ["e", "op", "id", "mapping", "composition", "_n", "_log", "_size", "tree", "lazy"]

    def __init__(self,
                 a: List[S],
                 e: S,
                 op: Callable[[S, S], S],
                 id_: F,
                 mapping: Callable[[F, S], S],
                 composition: Callable[[F, F], F]) -> None:
        self.e = e
        self.op = op
        self.id = id_
        self.mapping = mapping
        self.composition = composition

        self._n = len(a)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log

        self.tree = [e] * self._size + a + [e] * (self._size - self._n)
        for i in range(self._size - 1, 0, -1):
            self._update(i)

        self.lazy = [id_] * self._size

    def _update(self, k: int) -> None:
        """Update the value of a[k]."""
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def _apply_all(self, k: int, f: F) -> None:
        self.tree[k] = self.mapping(f, self.tree[k])
        if k < self._size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def _push(self, k: int) -> None:
        self._apply_all(2 * k, self.lazy[k])
        self._apply_all(2 * k + 1, self.lazy[k])
        self.lazy[k] = self.id

    def set(self, k: int, x: S) -> None:
        """Assign x to a[k] in O(log n)."""
        assert 0 <= k < self._n

        k += self._size
        for i in range(self._log, 0, -1):
            self._push(k >> i)
        self.tree[k] = x
        for i in range(1, self._log + 1):
            self._update(k >> i)

    def get(self, k: int) -> S:
        """Return a[k] in O(1)."""
        assert 0 <= k < self._n

        k += self._size
        for i in range(self._log, 0, -1):
            self._push(k >> i)
        return self.tree[k]

    def prod(self, l: int, r: int) -> S:
        """Return op(a[l], ..., a[r - 1]). Return e, if l == r.
        Complexity: O(log n)
        """
        assert 0 <= l <= r <= self._n

        if l == r:
            return self.e

        l += self._size
        r += self._size
        for i in range(self._log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push(r >> i)

        sml, smr = self.e, self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.tree[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def prod_all(self) -> S:
        """Return op(a[0], ..., a[n - 1]. Return e if n == 0.
        Complexity: O(1)
        """
        return self.tree[1]

    def apply(self, k: int, f: F) -> None:
        """Apply a[p] = op_st(a[p], x) in O(log n)."""
        assert 0 <= k < self._n

        k += self._size
        for i in range(self._log, 0, -1):
            self._push(k >> i)
        self.tree[k] = self.mapping(f, self.tree[k])
        for i in range(1, self._log + 1):
            self._update(k >> i)

    def apply_range(self, l: int, r: int, f: F) -> None:
        """Apply a[i] = op_st(a[i], x) for all i = l..r-1 in O(log n)."""
        assert 0 <= l <= r <= self._n

        if l == r:
            return

        l += self._size
        r += self._size
        for i in range(self._log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)

        l_tmp, r_tmp = l, r
        while l < r:
            if l & 1:
                self._apply_all(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._apply_all(r, f)
            l >>= 1
            r >>= 1
        l, r = l_tmp, r_tmp

        for i in range(1, self._log + 1):
            if ((l >> i) << i) != l:
                self._update(l >> i)
            if ((r >> i) << i) != r:
                self._update((r - 1) >> i)

    def max_right(self, l: int, g: Callable[[S], bool]) -> int:
        """
        Return an index r satisfying both:
            1. r = l or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            2. r = n or f(op(a[l], a[l + 1], ..., a[r])) = false.

        If f is monotone, this is the maximum r satisfying:
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true.

        Complexity: O(log n)
        """
        assert 0 <= l <= self._n
        assert g(self.e)

        if l == self._n:
            return self._n

        l += self._size
        for i in range(self._log, 0, -1):
            self._push(l >> i)
        sm = self.e

        while True:
            while not l & 1:
                l >>= 1

            if not g(self.op(sm, self.tree[l])):
                while l < self._size:
                    l *= 2
                    if g(self.op(sm, self.tree[l])):
                        sm = self.op(sm, self.tree[l])
                        l += 1
                return l - self._size

            sm = self.op(sm, self.tree[l])
            l += 1

            if (l & -l) == l:
                break

        return self._n

    def min_left(self, r: int, g: Callable[[S], bool]) -> int:
        """
        Return an index l satisfying both:
            1. l = r or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            2. l = 0 or f(op(a[l - 1], a[l + 1], ..., a[r - 1])) = false.
        If f is monotone, this is the minimum l satisfying:
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true.

        Complexity: O(log n)
        """
        assert 0 <= r <= self._n
        assert g(self.e)

        if not r:
            return 0

        r += self._size
        for i in range(self._log, 0, -1):
            self._push((r - 1) >> i)
        sm = self.e

        while True:
            r -= 1
            while r > 1 and r & 1:
                r >>= 1

            if not g(self.op(self.tree[r], sm)):
                while r < self._size:
                    r = 2 * r + 1
                    if g(self.op(self.tree[r], sm)):
                        sm = self.op(self.tree[r], sm)
                        r -= 1
                return r + 1 - self._size

            sm = self.op(self.tree[r], sm)

            if (r & -r) == r:
                break

        return 0


def op(l, r):
    return [l[0] + r[0], l[1] + r[1], l[2] + r[2] + l[1] * r[0]]


def mapping(f, x):
    if not f:
        return x
    return [x[1], x[0], x[0] * x[1] - x[2]]


N, Q = map(int, input().split())
A = list(map(int, input().split()))
dic = {0: [1, 0, 0], 1: [0, 1, 0]}

lst = LazySegmentTree([dic[v] for v in A], [0, 0, 0], op, False, mapping, xor)

for i in range(Q):
    T, L, R = map(int, input().split())
    if T == 1:
        lst.apply_range(L-1, R, True)
    else:
        print(lst.prod(L-1, R)[2])
