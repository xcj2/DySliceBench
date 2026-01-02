import math
from collections import deque


class SegmentTree:
    __slots__ = ["elem_size", "tree_size", "tree", "lazy"]

    def __init__(self, a: list, default: int):
        real_size = len(a)
        self.elem_size = 1 << math.ceil(math.log2(real_size))
        self.tree_size = 2 * self.elem_size
        self.tree = [default]*self.elem_size + a + [default]*(self.elem_size - real_size)
        self.lazy = [None]*self.tree_size
        self.init_tree()

    def init_tree(self):
        tree = self.tree
        for i in range(self.elem_size-1, 0, -1):
            left, right = tree[i << 1], tree[(i << 1)+1]
            # ===== change me =====
            tree[i] = left if left < right else right

    def get_indexes(self, l: int, r: int):
        '''[x, y)'''
        l, r, targets, path, p_l, p_r = l+self.elem_size, r+self.elem_size, deque(), deque(), 0, 0
        t_ap, p_ap = targets.append, path.appendleft

        while l < r:
            if l & 1:
                t_ap(l)
                p_l = p_l or l >> 1
                l += 1
            if r & 1:
                r -= 1
                t_ap(r)
                p_r = p_r or r >> 1
            l >>= 1
            r >>= 1

        deepest = (p_l, p_r)

        while p_l > 1 or p_r > 1:
            if p_r != p_l > 1:
                p_ap(p_l)
            p_l >>= 1
            if p_r > 1:
                p_ap(p_r)
                p_r >>= 1

        #print(targets, path)
        return targets, path, deepest

    def propagate(self, indexes: list, value: int = None):
        tree, lazy, elem_size = self.tree, self.lazy, self.elem_size
        if value is None:
            for n in indexes:
                if lazy[n] is None:
                    continue
                tree[n] = lazy[n]
                if n < elem_size:
                    lazy[n << 1] = lazy[(n << 1)+1] = lazy[n]
                lazy[n] = None
        else:
            for n in indexes:
                if n < elem_size:
                    lazy[n << 1] = lazy[(n << 1)+1] = value
                tree[n] = value
                lazy[n] = None

    def update_lazy(self, l, r, value):
        targets, paths, deepest = self.get_indexes(l, r)
        self.propagate(paths)
        self.propagate(targets, value)
        self.update_tree(deepest)

    def get_value(self, l: int, r: int):
        tree = self.tree
        targets, paths, deepest = self.get_indexes(l, r)
        self.propagate(paths)
        self.propagate(targets)
        self.update_tree(deepest)

        # ===== change me =====
        return min(tree[n] for n in targets)

    def update_tree(self, indexes: tuple):
        ''' ????????????lazy?????¨????????¬????????§???????????¨???????????¨???????????? '''

        tree, lazy = self.tree, self.lazy

        for k in indexes:
            #if k >= self.elem_size:
            #    k >>= 1

            while k > 0:
                left, right = k << 1, (k << 1)+1
                # ===== change me =====
                if lazy[left] is not None:
                    tree[left] = lazy[left]
                if lazy[right] is not None:
                    tree[right] = lazy[right]
                tree[k] = tree[left] if tree[left] < tree[right] else tree[right]

                k >>= 1

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
append = ans.append
for _ in [0]*q:
    l = list(map(int, input().split()))
    if l[0] == 0:
        rmq.update_lazy(l[1], l[2]+1, l[3])
    else:
        a = rmq.get_value(l[1], l[2]+1)
        append(a)

print("\n".join([str(n) for n in ans]))