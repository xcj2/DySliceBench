import math
import sys

class SegmentTree(object):
    __slots__ = ["elem_size", "tree", "default"]

    def __init__(self, a: list, default: int):
        real_size = len(a)
        self.elem_size = elem_size = 1 << math.ceil(math.log2(real_size))
        self.tree = tree = [default] * (elem_size * 2)
        tree[elem_size:elem_size+real_size] = a
        self.default = default

        for i in range(elem_size - 1, 0, -1):
            l, r = tree[i<<1], tree[(i<<1)+1]
            tree[i] = l if l < r else r

    def get_value(self, x: int, y: int) -> int:
        l, r = x + self.elem_size, y + self.elem_size
        tree, result = self.tree, self.default
        while l < r:
            if l & 1:
                if tree[l] < result:
                    result = tree[l]
                l += 1
            if r & 1:
                r -= 1
                if tree[r] < result:
                    result = tree[r]
            l, r = l >> 1, r >> 1

        return result

    def set_value(self, i: int, value: int) -> None:
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)

    def update(self, i: int) -> None:
        tree = self.tree
        while i > 1:
            i >>= 1
            l, r = tree[i<<1], tree[(i<<1)+1]
            tree[i] = l if l < r else r
 
n, q = map(int, input().split())
tree = SegmentTree([2**31-1]*n, 2**31-1)
ans = []
append = ans.append
for com, x, y in (map(int, l.split()) for l in sys.stdin.readlines()):
    if com == 0:
        tree.set_value(x, y)
    else:
        append(tree.get_value(x, y+1))
print(*ans, sep="\n")
