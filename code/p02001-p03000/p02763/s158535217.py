# E - Simple String Queries
from operator import or_


class SegmentTree:
    __slots__ = ["_default_value", "_seg_func", "_modifying_func", "_size", "_tree"]

    def __init__(self, initial_values: "Sequence", default_value: "Union[int, str]", seg_func: "Callable",
                 modifying_func: "Optional[Callable]" = None) -> None:
        self._default_value = default_value
        self._seg_func = seg_func
        self._modifying_func = modifying_func
        self._size = 1 << (len(initial_values) - 1).bit_length()
        self._tree = self._build(initial_values)

    def _build(self, initial_values: "Sequence") -> "List":
        """Build a segment tree with initial values."""
        tree = [self._default_value] * (2 * self._size)

        if self._modifying_func:
            initial_values = map(self._modifying_func, initial_values)

        for idx, val in enumerate(initial_values):  # set a tree
            tree[idx + self._size - 1] = val

        for idx in range(self._size - 2, -1, -1):  # build
            tree[idx] = self._seg_func(tree[2 * idx + 1], tree[2 * idx + 2])

        return tree

    def update(self, index: int, value: int) -> None:
        """Update index to value."""
        index += self._size - 1
        if self._modifying_func:
            value = self._modifying_func(value)
        self._tree[index] = value
        while index:
            index = (index - 1) // 2
            self._tree[index] = self._seg_func(self._tree[2 * index + 1], self._tree[2 * index + 2])

    def query(self, left: int, right: int) -> "Union[int, str]":
        """Respond to query in [left, right]."""
        left += self._size
        right += self._size
        result = self._default_value
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
    _, S, _, *queries = open(0).read().split()
    tree = SegmentTree(S, 0, or_, lambda c: 1 << (ord(c) - 97))
    ans = []
    popcount = lambda x: bin(x).count("1")
    for com, a, b in zip(*[iter(queries)] * 3):
        if com == "1":
            tree.update(int(a) - 1, b)
        else:
            ans.append(popcount(tree.query(int(a) - 1, int(b))))
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
