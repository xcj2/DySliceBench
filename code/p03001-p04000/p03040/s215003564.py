from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 18
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


class BIT:
    def __init__(self, size):
        self.bit = [0] * size
        self.size = size
        self.total = 0

    def add(self, i, w):
        x = i + 1
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        self.total += w
        return

    def sum(self, i):
        res = 0
        x = i + 1
        while x:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def interval_sum(self, i, j): # i <= x < j の区間
        return self.sum(j - 1) - self.sum(i - 1)

    def search(self, k):
        if k > self.total:
            return -1
        if k == 0:
            return 0
        step = 1 << (self.size.bit_length() - 1)
        now_index = 0
        ret = 0
        while step:
            if now_index + step < self.size and ret + self.bit[now_index + step - 1] < k:
                ret += self.bit[now_index + step - 1]
                now_index += step
            step >>= 1
        # now_indexを伸ばしいって、sumがk以上に達する直前まで伸ばし続けるならreturnのところでnow_index - 1。
        # その場合、bit.sum(now_index - 1) <= k < bit.sum(now_index)
        # 達してすぐのindexであれば-1しない
        return now_index


q = I()
query = []
A = []
for _ in range(q):
    l = LI()
    if l[0] == 1:
        A += [l[1]]
    query += [l]



ind_to_co = sorted(A)
co_to_ind = {}
for i, x in enumerate(ind_to_co):
    co_to_ind[x] = i


bit1 = BIT(len(A))
bit2 = BIT(len(A))
n = 0
B = 0
for l in query:
    if l[0] == 1:
        B += l[2]
        bit1.add(co_to_ind[l[1]], 1)
        bit2.add(co_to_ind[l[1]], l[1])
        n += 1
    else:
        min_ind = bit1.search(n // 2 + bool(n % 2))
        d = n // 2 + bool(n % 2)
        min_val = bit2.interval_sum(min_ind + 1, bit2.size) - bit1.interval_sum(min_ind + 1, bit1.size) * ind_to_co[min_ind] \
            + bit1.sum(min_ind - 1) * ind_to_co[min_ind] - bit2.sum(min_ind - 1) + B
        print(ind_to_co[min_ind], min_val)