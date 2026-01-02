from operator import add


class SegmentTreeClass:
    def __init__(self,
                 init_val: 'initial value: iterable',
                 segfunc: 'operation unique in case',
                 ide_ele: 'identity element corresponding init_val' = 0,
                 ):
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.size = 1 << (len(init_val) - 1).bit_length()
        self.tree = self._build(init_val)

    def _build(self, init_val) -> 'tree':
        segfunc = self.segfunc

        tree = [self.ide_ele] * (self.size * 2 - 1)

        for idx, val in enumerate(init_val, self.size - 1):  # set
            # modify val if needed (e.g. str -> ord())
            tree[idx] = val

        for idx in range(self.size - 2, -1, -1):  # build
            tree[idx] = segfunc(tree[idx * 2 + 1], tree[idx * 2 + 2])

        return tree

    def update(self, idx: int, val) -> None:
        tree = self.tree
        segfunc = self.segfunc

        idx += self.size - 1
        # modify val if needed as same as in _build()
        tree[idx] = val
        while idx > 0:
            idx = (idx - 1) // 2
            tree[idx] = segfunc(tree[idx * 2 + 1], tree[idx * 2 + 2])

    def query(self, left: int, right: int) -> 'result':
        left += self.size
        right += self.size
        ret = self.ide_ele  # left >= right: return self.ide_ele
        segfunc = self.segfunc
        tree = self.tree
        while left < right:  # どの段も奇偶...順
            if left & 1:  # odd
                ret = segfunc(ret, tree[left - 1])
                left += 1
            if right & 1:  # odd
                right -= 1
                ret = segfunc(ret, tree[right - 1])
            left >>= 1
            right >>= 1
        return ret


L = 10
n = int(input())
s = map(int, input())

d1 = [0] * L
s1 = SegmentTreeClass(init_val=d1, segfunc=add, ide_ele=0)
d2 = [0] * L
s2 = SegmentTreeClass(init_val=d1, segfunc=add, ide_ele=0)
d3 = [0] * L
s3 = SegmentTreeClass(init_val=d1, segfunc=add, ide_ele=0)

for c in s:
    x = s2.query(0, L)
    s3.update(c, x)

    x = s1.query(0, L)
    s2.update(c, x)

    s1.update(c, 1)

print(s3.query(0, L))

# O(3*N)分からない
