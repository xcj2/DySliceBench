# https://atcoder.jp/contests/abc157/tasks/abc157_e

import sys
input = sys.stdin.readline


class SegmentTree:

    def __init__(self, n, op, e):
        """
        :param n: 要素数
        :param op: 二項演算
        :param e: 単位減
        例) 区間最小値  SegmentTree(n, lambda a, b : a if a < b else b, 10 ** 18)
            区間和     SegmentTree(n, lambda a, b : a + b, 0)
        """
        self.n = n
        self.op = op
        self.e = e
        self.size = 1 << (self.n - 1).bit_length()      # st[self.size + i] = array[i]
        self.tree = [self.e] * (self.size << 1)

    def built(self, array):
        """arrayを初期値とするセグメント木を構築"""
        for i in range(self.n):
            self.tree[self.size + i] = array[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.op(self.tree[i << 1], self.tree[(i << 1) + 1])

    def update(self, i, x):
        """i 番目の要素を x に更新"""
        i += self.size
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.op(self.tree[i << 1], self.tree[(i << 1) + 1])

    def get_val(self, l, r):
        """[l, r)の畳み込みの結果を返す"""
        l, r = l + self.size, r + self.size
        res = self.e
        while l < r:
            if l & 1:
                res = self.op(self.tree[l], res)
                l += 1
            if r & 1:
                r -= 1
                res = self.op(self.tree[r], res)
            l, r = l >> 1, r >> 1
        return res


##################################################################################################################

def popcount(x):
    return bin(x).count("1")

N = int(input())
st = SegmentTree(N, lambda a, b: a | b, 0)
S = input().strip()
data = []
for s in S:
    data.append(1 << (ord(s) - ord("a")))
st.built(data)
Q = int(input())
for _ in range(Q):
    q, a, b = input().split()
    if q == "1":
        st.update(int(a)-1, 1 << (ord(b) - ord("a")))
    if q == "2":
        a = int(a) - 1
        b = int(b)
        print(popcount(st.get_val(a, b)))