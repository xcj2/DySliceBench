#!/usr/bin/env python3

import sys


INIT_VAL = 2 ** 31 - 1
REC_LIMIT = 100000


class SegmentTree4RMQ(object):

    def __init__(self, num_elems, init_val=sys.maxsize):
        self.num_elems = 1
        while self.num_elems < num_elems:
            self.num_elems *= 2
        self.data = [init_val for _ in range(self.num_elems * 2 - 1)]

    def update(self, k, a):
        k += self.num_elems - 1
        self.data[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = min(self.data[k * 2 + 1], self.data[k * 2 + 2])

    def rec(self, start, end, k, left, right):
        if right <= start or end <= left:
            return sys.maxsize
        elif start <= left and right <= end:
            return self.data[k]
        else:
            vl = self.rec(start, end, k * 2 + 1, left, (left + right) // 2)
            vr = self.rec(start, end, k * 2 + 2, (left + right) // 2, right)
            return min(vl, vr)

    def query(self, start, end):
        return self.rec(start, end, 0, 0, self.num_elems)


def main():
    sys.setrecursionlimit(REC_LIMIT)
    n, q = map(int, input().split())
    st = SegmentTree4RMQ(n, INIT_VAL)
    for _ in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            st.update(x, y)
        elif c == 1:
            print(st.query(x, y + 1))


if __name__ == '__main__':
    main()