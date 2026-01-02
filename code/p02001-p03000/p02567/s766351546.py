from math import ceil, log

class SegmentTree(object):
    __slots__ = ["elem_size", "tree", "default", "op"]

    def __init__(self, a: list, default: int, op):
        real_size = len(a)
        self.elem_size = elem_size = 1 << ceil(log(real_size, 2))
        self.tree = tree = [default] * (elem_size * 2)
        tree[elem_size:elem_size + real_size] = a
        self.default = default
        self.op = op

        for i in range(elem_size - 1, 0, -1):
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])

    def get(self, x: int, y: int) -> int:  # [x, y)
        l, r = x + self.elem_size, y + self.elem_size
        tree, result, op = self.tree, self.default, self.op
        while l < r:
            if l & 1:
                result = op(tree[l], result)
                l += 1
            if r & 1:
                r -= 1
                result = op(tree[r], result)
            l, r = l >> 1, r >> 1

        return result

    def set(self, i: int, value: int) -> None:
        k = self.elem_size + i
        self.tree[k] = value
        self.__update(k)

    def __update(self, i: int) -> None:
        op, tree = self.op, self.tree
        while i > 1:
            i >>= 1
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])

    def bisect_left(self, x: int, y: int, op):  # [x, y)
        l = x
        r = y + 1
        while l + 1 != r:
            mid = (l + r) // 2
            if op(seg.get(l, mid)):
                r = mid
            else:
                l = mid
        return r


N, Q = map(int, input().split())
A = list(map(int, input().split()))

seg = SegmentTree(A, 0, max)

for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        seg.set(a-1, b)
    elif t == 2:
        print(seg.get(a-1, b))
    else:
        print(seg.bisect_left(a-1, N, lambda x: x >= b))
