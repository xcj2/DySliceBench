from typing import Callable, Iterator, List, Optional, Sequence, Union


class LazySegmentTree:
    """Segment Tree with Lazy Propagation"""

    __slots__ = [
        "_identity",
        "_seg_func",
        "_modifying_func",
        "_level",
        "_size",
        "_tree",
        "_lazy",
    ]

    def __init__(
        self,
        initial_values: Sequence,
        identity: Union[int, str],
        seg_func: Callable,
        modifying_func: Optional[Callable] = None,
    ) -> None:
        self._identity = identity
        self._seg_func = seg_func
        self._modifying_func = modifying_func
        self._level = (len(initial_values) - 1).bit_length()
        self._size = 1 << self._level
        self._tree = self._build(initial_values)
        self._lazy: List[Optional[Union[int, str]]] = [None] * (2 * self._size)

    def _build(self, initial_values: Sequence) -> List[Union[int, str]]:
        """Build a segment tree with initial values."""
        tree = [self._identity] * (2 * self._size)

        if self._modifying_func:
            initial_values = map(self._modifying_func, initial_values)

        for idx, val in enumerate(initial_values):  # set a tree
            tree[idx + self._size - 1] = val

        for idx in range(self._size - 2, -1, -1):  # build
            tree[idx] = self._seg_func(tree[2 * idx + 1], tree[2 * idx + 2])

        return tree

    def _generate_indices(self, initial_left: int, initial_right: int) -> Iterator[int]:
        """Generate indices to propagate."""
        left = (initial_left + self._size) >> 1
        right = (initial_right + self._size) >> 1
        lc = 0 if initial_left & 1 else (left & -left).bit_length()
        rc = 0 if initial_right & 1 else (right & -right).bit_length()

        for i in range(self._level):
            if lc <= i:
                yield left
            if rc <= i:
                yield right
            left >>= 1
            right >>= 1

    def _propagate(self, *indices: int) -> None:
        """Propagate a given section."""
        for i in reversed(indices):
            value = self._lazy[i - 1]
            if value is not None:
                self._tree[2 * i - 1] = self._tree[2 * i] = value
                self._lazy[2 * i - 1] = self._lazy[2 * i] = value
                self._lazy[i - 1] = None

    def update(self, left: int, right: int, value: Union[int, str]) -> None:
        """Update [left, right] to value."""
        right += 1  # [left, right] == [left, right + 1)
        if self._modifying_func:
            value = self._modifying_func(value)
        (*indices,) = self._generate_indices(left, right)
        self._propagate(*indices)
        left += self._size
        right += self._size
        while left < right:
            if left & 1:
                self._lazy[left - 1] = self._tree[left - 1] = value
                left += 1
            if right & 1:
                right -= 1
                self._lazy[right - 1] = self._tree[right - 1] = value
            left >>= 1
            right >>= 1

        for i in indices:
            self._tree[i - 1] = self._seg_func(self._tree[2 * i - 1], self._tree[2 * i])

    def query(self, left: int, right: int) -> Union[int, str]:
        """Respond to query in [left, right]."""
        right += 1  # [left, right] == [left, right + 1)
        self._propagate(*self._generate_indices(left, right))
        left += self._size
        right += self._size
        result = self._identity
        while left < right:
            if left & 1:
                result = self._seg_func(result, self._tree[left - 1])
                left += 1
            if right & 1:
                right -= 1
                result = self._seg_func(result, self._tree[right - 1])
            left >>= 1
            right >>= 1
        return result


def main():
    # https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_F
    import sys

    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    N, _ = map(int, readline().split())
    tree = LazySegmentTree([2 ** 31 - 1] * N, 2 ** 31 - 1, min)
    ans = []
    for query in readlines():
        com, *info = map(int, query.split())
        if com:
            ans.append(tree.query(*info))
        else:
            tree.update(*info)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
