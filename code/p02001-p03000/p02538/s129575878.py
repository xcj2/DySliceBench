from typing import Callable, List, TypeVar

S = TypeVar("S")  # 作用付きモノイドの型
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


N, Q = map(int, input().split())

MOD = 998244353
MASK = 1 << 32

base = [MASK + 1] * N

tens = [0] * (N+1)
tens[0] = 1
for i in range(1, N+1):
    tens[i] = (tens[i-1] * 10) % MOD

ones = [0] * (N+1)
ones[1] = 1
for i in range(2, N+1):
    ones[i] = (ones[i-1] * 10 + 1) % MOD


def op(l, r):
    l0, l1 = l >> 32, l % MASK
    r0, r1 = r >> 32, r % MASK

    return (((l0 * tens[r1] + r0) % MOD) << 32) + (l1 + r1)


def mapping(l, r):
    if l == 0:
        return r

    r0, r1 = r >> 32, r % MASK
    return (((l * ones[r1]) % MOD) << 32) + r1


def composition(l, r):
    if l == 0:
        return r
    return l


seg = LazySegmentTree(base, 0, op, 0, mapping, composition)

for i in range(Q):
    L, R, D = map(int, input().split())
    seg.apply_range(L-1, R, D)
    print(seg.prod_all() >> 32)
