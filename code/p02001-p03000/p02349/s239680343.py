#!/usr/bin/env python3
# DSL_2_E: Range Add Query


class SegmentTree:
    INITIAL_VALUE = 0

    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.size = 2*size - 1
        self.data = [self.INITIAL_VALUE] * self.size

    def add(self, i, j, v):
        def _add(r, lo, hi):
            if hi < i or lo > j:
                return
            elif i <= lo and hi <= j:
                self.data[r] += v
            else:
                mid = lo + (hi - lo)//2
                _add(r*2 + 1, lo, mid)
                _add(r*2 + 2, mid+1, hi)

        return _add(0, 0, self.size//2)

    def get(self, i):
        def _get(r, lo, hi, v):
            v += self.data[r]
            if lo == hi:
                return v
            mid = lo + (hi - lo)//2
            if mid >= i:
                return _get(r*2 + 1, lo, mid, v)
            else:
                return _get(r*2 + 2, mid+1, hi, v)

        return _get(0, 0, self.size//2, 0)


def run():
    n, q = [int(i) for i in input().split()]
    tree = SegmentTree(n)

    for _ in range(q):
        com, *args = [i for i in input().split()]
        if com == '0':
            s, t, x = [int(i) for i in args]
            tree.add(s-1, t-1, x)

        elif com == '1':
            t = int(args[0])
            print(tree.get(t-1))
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

