from typing import Callable, List, Union

T = Union[int, str]


class SegmentTree:
    """Segment Tree"""

    __slots__ = ["_n", "_log", "_size", "op", "e", "tree"]

    def __init__(self, initial_values: List[T], op: Callable[[T, T], T], e: T) -> None:
        self._n = len(initial_values)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self.op = op
        self.e = e

        self.tree = [e] * 2 * self._size
        for i, a in enumerate(initial_values, self._size):
            self.tree[i] = a
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k: int) -> None:
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def get(self, k: int) -> T:
        assert 0 <= k < self._n
        return self.tree[k + self._size]

    def set(self, p: int, x: T) -> None:
        assert 0 <= p < self._n

        p += self._size
        self.tree[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def prod(self, l: int, r: int) -> T:
        assert 0 <= l <= r <= self._n

        sml, smr = self.e, self.e
        l += self._size
        r += self._size

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

    def prod_all(self) -> T:
        return self.tree[1]

    def max_right(self, l: int, f: Callable[[T], bool]) -> int:
        assert 0 <= l <= self._n
        assert f(self.e)

        if l == self._n:
            return self._n

        l += self._size
        sm = self.e

        while True:
            while not l & 1:
                l >>= 1

            if not f(self.op(sm, self.tree[l])):
                while l < self._size:
                    l *= 2
                    if f(self.op(sm, self.tree[l])):
                        sm = self.op(sm, self.tree[l])
                        l += 1
                return l - self._size

            sm = self.op(sm, self.tree[l])
            l += 1

            if (l & -l) == l:
                break

        return self._n

    def min_left(self, r: int, f: Callable[[T], bool]) -> int:
        assert 0 <= r <= self._n
        assert f(self.e)

        if not r:
            return 0

        r += self._size
        sm = self.e

        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1

            if not f(self.op(self.tree[r], sm)):
                while r < self._size:
                    r = 2 * r + 1
                    if f(self.op(self.tree[r], sm)):
                        sm = self.op(self.tree[r], sm)
                        r -= 1
                return r + 1 - self._size

            if (r & -r) == r:
                break

        return 0


def practice2_j():
    N, _, *AQ = map(int, open(0).read().split())
    A, Q = AQ[:N], AQ[N:]
    tree = SegmentTree(A, max, -1)
    res = []
    for t, x, y in zip(*[iter(Q)] * 3):
        if t == 1:
            tree.set(x - 1, y)
        elif t == 2:
            res.append(tree.prod(x - 1, y))
        else:
            res.append(tree.max_right(x - 1, lambda n: n < y) + 1)
    print("\n".join(map(str, res)))


if __name__ == "__main__":
    practice2_j()
