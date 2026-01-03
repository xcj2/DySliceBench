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
from operator import mul
from functools import reduce
import pprint
sys.setrecursionlimit(10 ** 9)


INF = 10 ** 13
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
        self.total += w
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
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

n = I()
A = LI()
val_idx = {A[j]:j+1 for j in range(n)}
bit = BIT(n + 2)
bit.add(n + 1, 1)
bit.add(0, 1)
ans = 0
for k in range(1, n + 1):
    idx = val_idx[k]
    bit.add(idx, 1)
    m = bit.sum(idx)
    r = bit.search(m + 1)
    l = bit.search(m - 1)
    ans += (r - idx) * (idx - l) * k

print(ans)