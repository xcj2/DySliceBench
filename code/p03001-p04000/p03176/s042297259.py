#!/usr/bin/env python3
import sys
INF = float("inf")
import math


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s = max(s, self.tree[i])
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = max(self.tree[i], x)
            i += i & -i


def solve(N: int, h: "List[int]", a: "List[int]"):

    seg = Bit(N+1)

    for i in range(N):
        temp = a[i] + seg.sum(h[i])
        seg.add(h[i], temp)
    print(seg.sum(N+1))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, h, a)


if __name__ == '__main__':
    main()
