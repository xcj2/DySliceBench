import sys
fin = sys.stdin.readline


class SegmentTree(object):
    INT_MAX = (1 << 31) - 1

    def __init__(self, n_):
        n = 1
        while n < n_:
            n *= 2
        self._tree = [self.INT_MAX] * (n * 2 - 1)
        self.num_elems = n


    def update(self, k, a):
        # accessing the index corresponding to the leaf
        k += self.num_elems - 1
        self._tree[k] = a

        # climbing up
        while k > 0:
            k = (k - 1) // 2
            self._tree[k] = min(self._tree[k * 2 + 1], self._tree[k * 2 + 2])
        # print(self._tree)

    def query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.INT_MAX
        
        if (a <= l and r <= b):
            return self._tree[k]
        else:
            m = (l + r) // 2
            vl = self.query(a, b, 2 * k + 1, l, m)
            vr = self.query(a, b, 2 * k + 2, m, r)
            # print(vl, vr)
            return min(vl, vr)
    

n, q = [int(elem) for elem in fin().split()]
segtree = SegmentTree(n)

ceil_exp_2 = 1
while ceil_exp_2 < n:
    ceil_exp_2 *= 2

queries = tuple(tuple(int(elem) for elem in fin().split()) for _ in range(q))

for c, x, y in queries:
    if c == 0:
        segtree.update(x, y)
    else:
        print(segtree.query(x, y + 1, 0, 0, ceil_exp_2))

