#!/usr/bin/env python3
import sys
INF = float("inf")

import math


class SegmentTree(object):
    # セグメント木

    def __init__(self, N):
        """サイズNの配列を元にしたセグメント木
        """
        # 単位元
        self.idelem = 0
        # 比較関数

        def f(a, b):
            return a | b

        self.func = f

        self.N0 = 1
        while self.N0 < N:
            self.N0 <<= 1
        self.tree = [self.idelem]*(2*self.N0)

    def update(self, k, x):
        """k番目の値をxに更新
        """
        k += self.N0-1
        self.tree[k] = x
        while k > 1:
            k = (k-1)//2
            self.tree[k] = self.func(self.tree[2*k+1], self.tree[2*k+2])

    def query(self, l, r):
        """区間[l, r)の最小値
        """
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


def bit_sum(n):
    wa = 0
    while n > 0:
        wa += n & 1
        n >>= 1
    return wa


def main():
    N = int(input())
    S = input()
    Q = int(input())
    query = [input().split() for i in range(Q)]

    seg = SegmentTree(N)
    for i, c in enumerate(S):
        seg.update(i, 1 << (ord(c)-ord('a')))

    for q in query:
        if q[0] == "1":
            seg.update(int(q[1])-1, 1 << (ord(q[2])-ord('a')))
        else:
            ans = seg.query(int(q[1])-1, int(q[2]))
            print(bit_sum(ans))
    pass


if __name__ == '__main__':
    main()
