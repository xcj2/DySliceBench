import sys
import math
import string
import fractions
import random
from operator import itemgetter
import itertools
from collections import deque
import copy
import heapq
import bisect

MOD = 10 ** 9 + 7
INF = float('inf')
input = lambda: sys.stdin.readline().strip()


def func(a, b):
    if a | b == 0:
        return 0
    else:
        return 1


class SegmentTree:
    """
    各ノードが半開区間に対応した完全二分木。
    子は親を半分にした区間を持つ。
    構築O(n), 区間に対する操作O(logn), 値の更新O(logn)
    区間に対する操作は最小値, 最大値, 区間に対する和など柔軟に変更して用いよう！
    """

    def __init__(self, x, init_val):  # 構築, init_valは配列の初期値
        self.init_val = init_val
        self.length = 2 ** ((len(x) - 1).bit_length())
        self.data = [init_val] * 2 * self.length
        for i in range(len(x)):
            self.data[i + self.length - 1] = x[i]
        for i in range(self.length - 2, -1, -1):
            self.data[i] = func(self.data[2 * i + 1], self.data[2 * i + 2])

    def teach_current_val(self, index):
        return self.data[index + self.length - 1]

    def replace(self, index, val):  # indexの値をvalに更新
        index += self.length - 1
        self.data[index] = val
        while index:
            index = (index - 1) // 2
            self.data[index] = func(self.data[2 * index + 1], self.data[2 * index + 2])

    def query(self, left, right):  # 半開区間の最小値等を求める, 葉からさかのぼっていくイメージ。
        if right <= left:
            return self.init_val
        left += self.length - 1  # self.dataの位置に合わせる。
        right += self.length - 2  # self.dataの位置に合わせる。半開区間
        ans_ = self.init_val
        while right > left + 1:
            if left & 1 == 0:  # if left_index%2 == 0:
                ans_ = func(ans_, self.data[left])
            if right & 1 == 1:  # if right_index%2 == 1:
                ans_ = func(ans_, self.data[right])
                right -= 1
            left //= 2
            right = (right - 1) // 2
        if left == right:
            ans_ = func(ans_, self.data[left])
        else:
            ans_ = func(func(ans_, self.data[left]), self.data[right])
        return ans_


N = int(input())
S = input()
Q = int(input())
alphabets = string.ascii_lowercase
segs = []
check = dict()
for i in alphabets:
    segs.append([1 if S[l] == i else 0 for l in range(N)])
for i in range(26):
    segs[i] = SegmentTree(segs[i], 0)
for _ in range(Q):
    Query = list(map(str, input().split()))
    if Query[0] == "1":
        i, c = int(Query[1]), Query[2]
        if check.get(str(i - 1)):
            segs[ord(check[str(i - 1)]) - 97].replace(i - 1, 0)
            segs[ord(c) - 97].replace(i - 1, 1)
            check[str(i - 1)] = c
        else:
            segs[ord(S[i - 1]) - 97].replace(i - 1, 0)
            segs[ord(c) - 97].replace(i - 1, 1)
            check[str(i - 1)] = c
    else:
        l, r = map(int, (Query[1], Query[2]))
        ans = 0
        for i in segs:
            ans += i.query(l - 1, r)
        print(ans)
