#!/usr/bin/env python3
# DSL_2_F: RMQ and RUQ
# Range Minimum Query and Range Update Query


class SegmentTree:
    INITIAL_VALUE = 2**31 - 1
    DIVIDED = -1

    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.size = 2*size - 1
        self.data = [-1] * self.size
        self.data[0] = self.INITIAL_VALUE

    def set_range(self, lo, hi, v):
        def _set_range(r, i, j, vv):
            if j < lo or i > hi:
                if vv != self.DIVIDED:
                    self.data[r] = vv
            elif lo <= i and j <= hi:
                self.data[r] = v
            else:
                if self.data[r] != self.DIVIDED:
                    if vv == self.DIVIDED:
                        vv = self.data[r]
                    self.data[r] = self.DIVIDED
                mid = i + (j - i)//2
                _set_range(r*2 + 1, i, mid, vv)
                _set_range(r*2 + 2, mid+1, j, vv)

        _set_range(0, 0, self.size//2, self.DIVIDED)

    def min(self, i, j):
        def _min(r, lo, hi):
            if j < lo or i > hi:
                return self.INITIAL_VALUE
            elif self.data[r] != self.DIVIDED:
                return self.data[r]
            else:
                mid = lo + (hi - lo)//2
                return min(_min(r*2 + 1, lo, mid),
                           _min(r*2 + 2, mid+1, hi))

        return _min(0, 0, self.size//2)


def run():
    n, q = [int(i) for i in input().split()]

    tree = SegmentTree(n)

    for _ in range(q):
        com, *args = input().split()
        if com == '0':
            s, t, x = [int(i) for i in args]
            tree.set_range(s, t, x)
        elif com == '1':
            s, t = [int(i) for i in args]
            print(tree.min(s, t))


if __name__ == '__main__':
    run()

