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
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    d = dict((num, i) for i, num in enumerate(sorted(set(nums)), 1))
    # print(d)
    bit = BIT(n + 1)

    ans = 0
    for num in nums:
        bit.add(d[num], 1)
        # print(bit)
        ans += bit.sum(d[num] + 1, n + 1)

    print(ans)


if __name__ == "__main__":
    main()

