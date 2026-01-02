# coding:utf-8

import sys

INF = 2 ** 31 - 1
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]


class SegmentTree:
    __slots__ = ['node', 'size']

    def __init__(self, n_):
        self.size = 2 ** n_.bit_length()
        self.node = [INF] * (2 * self.size)

    # k番目の値をaに変更
    def update(self, k, a):
        k += self.size - 1
        self.node[k] = a
        # 登りながら更新
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = min(self.node[k * 2 + 1], self.node[k * 2 + 2])

    # [a, b)の最小値を求める
    def query(self, a, b):
        l, r = a + self.size, b + self.size
        res = INF
        while l < r:
            if r & 1:
                r -= 1
                res = min(res, self.node[r - 1])

            if l & 1:
                res = min(res, self.node[l - 1])
                l += 1

            l >>= 1
            r >>= 1
        return res


n, q = LI()
sgt = SegmentTree(n)

for _ in range(q):
    c, x, y = LI()

    if c == 0:
        sgt.update(x, y)
    else:
        print(sgt.query(x, y + 1))

