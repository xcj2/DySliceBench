#!/usr/bin/env python3
import sys
from bisect import bisect_left
MOD = 998244353  # type: int

import math


class SegmentTree(object):
    # セグメント木

    def __init__(self, N):
        """サイズNの配列を元にしたセグメント木
        """
        # 単位元
        self.idelem = -10**9
        # 比較関数
        self.func = max

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


def solve(N: int, X: "List[int]", D: "List[int]"):
    # グラフを構成しようとすると、O(N^2)が考えられる。
    # 接続先が単調に決まることを利用して、一番遠くだけ記憶しておく。
    reachable = [0]*N

    # ソートしておく
    X, D = zip(*sorted(zip(X, D)))
    # print(X, D)

    # O(NlogN)で直接的に影響範囲を整理する。
    for i, (x, d) in enumerate(zip(X, D)):
        reachable[i] = bisect_left(X, x+d)

    # SegmentTreeで、間接的な影響範囲を管理する
    seg = SegmentTree(N)

    # 後ろから、真の影響範囲を決めていく
    for v in reversed(range(N)):
        if v == N-1:
            seg.update(v, reachable[v])
            continue
        # vからreachable[v]-1までの間のノードの
        # 影響範囲の最大値が、真の影響範囲
        a = seg.query(v, reachable[v])
        if a > 0:
            seg.update(v, a)
        else:
            seg.update(v, v+1)

    true_reachable = [seg.query(v, v+1) for v in range(N)]

    # print(true_reachable)

    dp = [0]*(N+1)
    dp[N] = 1
    for v in reversed(range(N)):
        dp[v] = dp[v+1]+dp[true_reachable[v]]
        dp[v] %= MOD
    print(dp[0])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, X, D)


if __name__ == '__main__':
    main()
