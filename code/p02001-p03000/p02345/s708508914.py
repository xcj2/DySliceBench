import math


class SegmentTree:
    __slots__ = ["elem_size", "tree_size", "tree"]

    def __init__(self, a: list, default: int):
        real_size = len(a)
        self.elem_size = 1 << math.ceil(math.log2(real_size))
        self.tree_size = 2 * self.elem_size
        self.tree = [default]*self.elem_size + a + [default]*(self.elem_size - real_size)
        self.init_tree()

    def init_tree(self):
        tree = self.tree
        for i in range(self.elem_size-1, 0, -1):
            left, right = tree[i << 1], tree[(i << 1)+1]
            # ===== ??????????????´???????????? =====
            tree[i] = left if left < right else right

    def get_range_indexes(self, x: int, y: int):
        '''[x, y), tree[k], [l_end, r_end)'''
        l, r = x+self.elem_size, y+self.elem_size
        indexes = []
        append = indexes.append
        while l < r:
            if l & 1:
                append(l)
                l += 1
            if r & 1:
                r -= 1
                append(r)
            l, r = l >> 1, r >> 1

        return indexes

    def get_value(self, x: int, y: int):
        tree = self.tree
        index_list = self.get_range_indexes(x, y)

        # ===== ??????????????´???????????? =====
        return min(tree[n] for n in index_list)

    def update_tree(self, k: int):
        tree = self.tree

        while k > 1:
            k >>= 1
            left, right = tree[k << 1], tree[(k << 1)+1]
            # ===== ??????????????´???????????? =====
            tree[k] = left if left < right else right

    def set_value(self, i: int, value: int, op: str):
        k = self.elem_size + i
        if op == "=":
            self.tree[k] = value
        elif op == "+":
            self.tree[k] += value
        self.update_tree(k)


n, q = map(int, input().split())
rmq = SegmentTree([2**31-1]*n, 2**31-1)
ans = []
for _ in [0]*q:
    c, x, y = map(int, input().split())
    if c == 0:
        rmq.set_value(x, y, "=")
    else:
        ans.append(rmq.get_value(x, y+1))
print("\n".join([str(n) for n in ans]))