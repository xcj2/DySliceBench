class SegmentTree(object):
    INIT = 2 ** 31 - 1
    DIVIDED = -1

    def __init__(self, n: int) -> None:
        size = 1
        while size < n:
            size *= 2
        self.size = 2 * size - 1
        self.data = [-1] * self.size
        self.data[0] = self.INIT

    def set_range(self, l: int, h: int, v: int) -> None:
        def _set_range(r, i: int, j: int, vv: int) -> None:
            if (j < l or i > h):
                if vv != self.DIVIDED:
                    self.data[r] = vv
            elif (l <= i and j <= h):  # noqa: E741
                self.data[r] = v
            else:
                if self.data[r] != self.DIVIDED:
                    if vv == self.DIVIDED:
                        vv = self.data[r]
                    self.data[r] = self.DIVIDED
                mid = i + (j - i) // 2
                _set_range(r * 2 + 1, i, mid, vv)
                _set_range(r * 2 + 2, mid + 1, j, vv)

        _set_range(0, 0, self.size // 2, self.DIVIDED)

    def min(self, i: int, j: int) -> int:
        def _min(r, l: int, h: int) -> int:
            if (j < l or i > h):
                return self.INIT
            elif self.data[r] != self.DIVIDED:
                return self.data[r]
            else:
                mid = l + (h - l) // 2
                return min(_min(r * 2 + 1, l, mid),
                           _min(r * 2 + 2, mid + 1, h))

        return _min(0, 0, self.size // 2)


if __name__ == "__main__":
    n, q = map(lambda x: int(x), input().split())
    segtree = SegmentTree(n)

    for _ in range(q):
        com, *v = map(lambda x: int(x), input().split())
        if (0 == com):
            segtree.set_range(v[0], v[1], v[2])
        else:
            print(segtree.min(v[0], v[1]))

