# https://atcoder.jp/contests/abc014/submissions/3935971
class SegmentTree(object):
    __slots__ = ["elem_size", "tree", "default", "op"]
    def __init__(self, a: list, default: int, op):
        from math import ceil, log
        real_size = len(a)
        self.elem_size = elem_size = 1 << ceil(log(real_size, 2))
        self.tree = tree = [default] * (elem_size * 2)
        tree[elem_size:elem_size + real_size] = a
        self.default = default
        self.op = op
        for i in range(elem_size - 1, 0, -1):
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])

    def get_value(self, x: int, y: int) -> int:  # 半開区間
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

    def set_value(self, i: int, value: int) -> None:
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)

    def update(self, i: int) -> None:
        op, tree = self.op, self.tree
        while i > 1:
            i >>= 1
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])

from operator import itemgetter
N, M = map(int, input().split())
LRC = [list(map(int, input().split())) for _ in range(M)]
LRC.sort(key=itemgetter(0))

idx_LRC = 0
q = []

seg = SegmentTree([float("inf")] * (N+1), float("inf"), min)

seg.set_value(1, 0)
for v in range(1, N+1):
    d = seg.get_value(v, N+1)
    while idx_LRC < M:
        l, r, c = LRC[idx_LRC]
        if l <= v:
            seg.set_value(r, min(seg.tree[r+seg.elem_size], d + c))
            idx_LRC += 1
        else:
            break
ans = seg.tree[N+seg.elem_size]
print(ans if ans!=float("inf") else -1)
