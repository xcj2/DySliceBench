#!/usr/bin/env python3


class FenwickTree(object):

    def __init__(self, num_elems):
        self.num_elems = num_elems
        self.data = [0 for _ in range(num_elems)]

    def sum_to(self, end):
        s = 0
        i = end - 1
        while i >= 0:
            s += self.data[i]
            i = (i & (i + 1)) - 1
        return s

    def sum_range(self, start, end):
        return self.sum_to(end) - self.sum_to(start)

    def add(self, idx, x):
        while idx < self.num_elems:
            self.data[idx] += x
            idx |= idx + 1


def main():
    n, q = map(int, input().split())
    ft = FenwickTree(n)
    for _ in range(q):
        c, x, y = map(int, input().split())
        if c == 0:
            ft.add(x - 1, y)
        elif c == 1:
            print(ft.sum_range(x - 1, y))


if __name__ == '__main__':
    main()