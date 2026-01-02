# Range Sum Query
# https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_B
"""
Binary Indexed Tree (Fenwick Tree)

References:
    http://hos.ac/slides/20140319_bit.pdf

Verified:
    https://judge.yosupo.jp/problem/point_add_range_sum
    https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_b
"""
from typing import Optional, Sequence


class BinaryIndexedTree:
    __slots__ = ["_size", "_tree", "_is_zero_indexed"]

    def __init__(self, size: int, initial_values: Optional[Sequence[int]] = None, is_zero_indexed: bool = True):
        self._size = size
        self._tree = [0] * (self._size + 1)
        self._is_zero_indexed = is_zero_indexed
        if initial_values:
            self._build(initial_values)

    def _build(self, initial_values: Sequence[int]):
        for i, a in enumerate(initial_values):
            self.add(i, a)

    def add(self, index: int, value: int) -> None:
        """Add value to tree[index], O(logN)."""
        if self._is_zero_indexed:
            index += 1
        while index <= self._size:
            self._tree[index] += value
            index += index & -index

    def sum(self, index: int) -> int:
        """Return the sum of [1, index], O(logN)."""
        ret = 0
        while index > 0:
            ret += self._tree[index]
            index -= index & -index
        return ret

    def range_sum(self, left: int, right: int) -> int:
        """Return the range sum of [left, right], O(logN)."""
        if not self._is_zero_indexed:
            left -= 1
        return self.sum(right) - self.sum(left)


def main():
    N, Q, *queries = map(int, open(0).read().split())
    tree = BinaryIndexedTree(N, is_zero_indexed=False)
    result = []
    for com, x, y in zip(*[iter(queries)] * 3):
        if com:
            result.append(tree.range_sum(x, y))
        else:
            tree.add(x, y)
    print(*result, sep="\n")


if __name__ == "__main__":
    main()

