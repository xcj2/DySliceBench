import math
import sys

class SegmentTree(object):
    __slots__ = ["elem_size", "tree_size", "tree", "default", "op"]

    def __init__(self, a: list, default: int, op):
        real_size = len(a)
        self.elem_size = 1 << math.ceil(math.log2(real_size))
        self.tree_size = 2 * self.elem_size
        self.tree = tree = [default] * self.elem_size + a + [default] * (self.elem_size - real_size)
        self.default = default
        self.op = op

        for i in range(self.elem_size - 1, 0, -1):
            tree[i] = op(tree[i<<1], tree[(i<<1)+1])

    def get_value(self, x: int, y: int):
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

    def set_value(self, i: int, value: int):
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)

    def update(self, i: int):
        op, tree = self.op, self.tree
        while i > 1:
            i >>= 1
            tree[i] = op(tree[i<<1], tree[(i<<1) + 1])

if __name__ == "__main__":
    n, q = map(int, input().split())
    tree = SegmentTree([2**31-1]*n, 2**31-1, min)
    ans = []
    append = ans.append
    for com, x, y in (map(int, l.split()) for l in sys.stdin.readlines()):
        if com == 0:
            tree.set_value(x, y)
        else:
            append(tree.get_value(x, y+1))
    print(*ans, sep="\n")
