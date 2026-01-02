from itertools import accumulate
from math import ceil
N = int(input())
A = list(map(int, input().split()))


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= (i & -i)
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += (i & -i)

    def reset(self):
        self.bit = [0] * (self.size + 1)


# BIT準備
BIT = BinaryIndexedTree(N)
# 答えをにぶたん
lo, hi = -1, max(A) + 1  # sample2などに対応するためにhiを設定
while hi - lo > 1:
    m = (hi + lo) // 2

    # m以上かどうかで分類
    binary = [(1 if a >= m else -1) for a in A]
    binary = list(accumulate(binary))

    # BITの初期化
    BIT.reset()

    # 和が0以上となる連続部分列を数える
    tmp = 0

    # 転倒数っぽくやる
    binary_sorted = {b: i for i, b in enumerate(sorted(binary), start=1)}
    ans = 0
    for j, b in enumerate(binary):
        tmp += BIT.sum(binary_sorted[b]) + (b >= 0)
        BIT.add(binary_sorted[b], 1)

    # 連続する部分列の個数の半分以上和が0以上となる区間が存在するかで場合分け
    if tmp >= ceil(((N * (N + 1)) / 2) / 2):
        lo = m
    else:
        hi = m

print(lo)
