# -*- coding: utf-8 -*-
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class ACC_2D:
    """
    二次元累積わ
    """

    def __init__(self, W, H):
        """
        W:幅
        H:高さ
        """

        self.W = W
        self.H = H
        self.mat = [[0]*(W+1) for _ in range(H+1)]

    def add(self, row, col, val):
        """
        matの値を変更する(初期化)
        row:たて(0<=row<H)
        col:横(0<=col<W)
        val:mat[row][col]を初期化する値
        """
        self.mat[row+1][col+1] += val

    def build(self):
        """
        累積和を計算する
        """
        for row in range(1, self.H+1):
            for col in range(1, self.W+1):
                self.mat[row][col] += self.mat[row][col-1] + \
                    self.mat[row-1][col] - self.mat[row-1][col-1]

    def get_val(self, g_row, g_col, s_row, s_col):
        """
        ２点で囲まれる長方形の、累積和を求める
        gx,gyは含まれない
        """
        return self.mat[g_row][g_col] - self.mat[s_row][g_col] - self.mat[g_row][s_col] + self.mat[s_row][s_col]


def solve():
    N, K = map(int, input().split())
    K2 = 2*K

    ACC = ACC_2D(K2, K2)

    # handle input
    # 全てを2K*2Kに圧縮する
    for _ in range(N):
        x, y, s = input().split()
        # 2K * 2Kに収める
        x = int(x)
        y = int(y)
        if s == "W":
            y += K
        x %= K2
        y %= K2

        ACC.add(x, y, 1)

    # 累積和をとる
    ACC.build()

    ans = 0
    # 黒としてチェックする
    # dは希望に沿っている数
    # ほんとは0~2Kで探さないといけないけど、N-dをついでにチェックすることで、半分でよくなる
    for row in range(K + 1):
        for col in range(K + 1):
            # 区間に入っている点の数
            d = ACC.get_val(row+K, col, row, 0)
            d += ACC.get_val(row, col+K, 0, col)
            d += ACC.get_val(K2, col+K, row+K, col)
            d += ACC.get_val(row+K, K2, row, col+K)
            ans = max(ans, d, N-d)
    print(ans)


solve()
