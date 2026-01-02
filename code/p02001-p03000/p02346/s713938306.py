from array import array
import bisect
import collections
import heapq
import itertools
import operator
import sys


class BIT:
    def __init__(self, n):
        self.n = n
        self.arr = array("l", [0] * (n + 1))

    def __str__(self):
        return str(self.arr.tolist())

    def add(self, i, x):
        while i <= self.n:
            self.arr[i] += x
            i += i & -i

    def sum(self, i, j=None):
        if j is None:
            s = 0
            while i > 0:
                s += self.arr[i]
                i -= i & -i
            return s

        if i > j:
            raise ValueError

        return self.sum(j) - self.sum(i - 1)


def main():
    n, q = map(int, sys.stdin.readline().split())
    bit = BIT(n)

    for _ in range(q):
        query, x, y = map(int, sys.stdin.readline().split())
        if query == 0:
            bit.add(x, y)
        elif query == 1:
            print(bit.sum(x, y))
        else:
            raise ValueError


if __name__ == "__main__":
    main()

