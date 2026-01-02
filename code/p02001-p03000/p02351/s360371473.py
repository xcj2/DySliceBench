#!/usr/bin/env python3
# DSL_2_G: RSQ and RAQ
# Range Add Query and Range Sum Query


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (self.size+1)

    def add(self, i, v):
        while i <= self.size:
            self.bit[i] += v
            i += (i & -i)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s


class RangeQuery:
    def __init__(self, n):
        self.size = n
        self.bit1 = BinaryIndexedTree(n+1)
        self.bit2 = BinaryIndexedTree(n+1)

    def add(self, i, j, v):
        self.bit1.add(i, v * -i)
        self.bit1.add(j+1, v * (j+1))
        self.bit2.add(i, v)
        self.bit2.add(j+1, -v)

    def sum(self, i, j):
        s = self.bit1.sum(j+1) + (j+1)*self.bit2.sum(j+1)
        s -= self.bit1.sum(i) + i*self.bit2.sum(i)
        return s


def run():
    n, q = [int(i) for i in input().split()]

    r = RangeQuery(n)

    for _ in range(q):
        com, *args = input().split()
        if com == '0':
            s, t, x = [int(i) for i in args]
            r.add(s, t, x)
        elif com == '1':
            s, t = [int(i) for i in args]
            print(r.sum(s, t))


if __name__ == '__main__':
    run()

