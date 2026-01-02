from typing import Callable, Sequence, Union, List


class SegmentTree:
    __slots__ = ["default_value", "seg_func", "size", "tree"]

    def __init__(
        self,
        initial_values: Sequence,
        default_value: Union[int, str],
        seg_func: Callable,
    ) -> None:
        self.default_value = default_value
        self.seg_func = seg_func
        self.size = 1 << (len(initial_values) - 1).bit_length()
        self.tree = self._build(initial_values)

    def _build(self, initial_values) -> List:
        tree = [self.default_value] * (2 * self.size)

        for idx, val in enumerate(initial_values):  # set
            # modify val if needed (e.g. str -> ord())
            tree[idx + self.size - 1] = val

        for idx in range(self.size - 2, -1, -1):  # build
            tree[idx] = self.seg_func(tree[2 * idx + 1], tree[2 * idx + 2])
        return tree

    def update(self, idx: int, val: int) -> None:
        idx += self.size - 1
        # modify val if needed as same as in _build()
        self.tree[idx] = val
        while idx:
            idx = (idx - 1) // 2
            x, y = 2 * idx + 1, 2 * idx + 2
            self.tree[idx] = self.seg_func(self.tree[x], self.tree[y])

    def query(self, left: int, right: int) -> Union[int, str]:
        if left > right:  # corner case
            return self.default_value

        left += self.size
        right += self.size
        result = self.default_value
        while left < right:
            if left & 1:
                result = self.seg_func(result, self.tree[left - 1])
                left += 1
            if right & 1:
                right -= 1
                result = self.seg_func(result, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return result


def main():
    N, Q = map(int, input().split())
    tree = SegmentTree([2 ** 31 - 1] * N, 2 ** 31 - 1, min)
    ans = []
    for _ in range(Q):
        com, x, y = map(int, input().split())
        if com:
            ans.append(tree.query(x, y + 1))
        else:
            tree.update(x, y)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()

