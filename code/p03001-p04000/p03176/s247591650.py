#!/usr/bin/env python3
import sys
INF = float("inf")
import math


class SegmentTree(object):
    # セグメント木

    def __init__(self, N):
        # 単位元
        self.idelem = 0
        # 比較関数
        self.func = max

        self.N0 = 1
        while self.N0 < N:
            self.N0 *= 2
        self.tree = [self.idelem]*(2*self.N0)

    def update(self, k, x):
        k += self.N0-1
        self.tree[k] = x
        while k > 1:
            k = (k-1)//2
            self.tree[k] = self.func(self.tree[2*k+1], self.tree[2*k+2])

    def query(self, l, r):
        l += self.N0-1
        r += self.N0-1
        s = self.idelem
        while l < r:
            if r % 2 == 0:
                r -= 1
                s = self.func(s, self.tree[r])

            if l % 2 == 0:
                s = self.func(s, self.tree[l])
                l += 1
            l //= 2
            r //= 2
        return s

    def __str__(self):
        return str(self.tree[self.N0-1:-1])


def solve(N: int, h: "List[int]", a: "List[int]"):

    seg = SegmentTree(N+1)

    for i in range(N):
        temp = a[i] + seg.query(0, h[i])
        seg.update(h[i], temp)
    print(seg.query(0, N+1))
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
