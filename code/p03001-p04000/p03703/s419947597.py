def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    # a - 1の場所にwを追加する
    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    # a未満の数字が何個あるか
    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

    def lowerbound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x + 1

N, K = getNM()
A = getArray(N)

# 連続部分列: imos, 尺取り法, セグ木, 数え上げdpなどが使えそう
# 算術平均がK以上であるものは何個あるでしょうか？ 尺取りっぽい
# → 平均なので尺取りではない　{100, 1 100...100}みたいな場合

# 平均なので各項をKで引いて見ようか
# N, K = 3, 6
# A = [7, 5, 7] の場合
# A = [1, -1, 1]になる 累計が0以上のもの → これだとO(n2)かかる
# 右端rを決めた時にペアになる左端lはいくつあるか

# N, K = 7, 26
# A = [10, 20, 30, 40, 30, 20, 10]の時
# imos = [0, -16, -22, -18, -4, 0, -6, -22]
# l ~ r区間の平均 = imos[r] - imos[l - 1] これが0以上なら
# = imos[r] >= imos[l - 1]なら
# imos[b] - imos[a] >= 0になるペアがいくつあるかをO(n)で

# つまり
# bより左側にbより小さい数はいくつあるか

A = [i - K for i in A]
imos = [0]
for i in range(N):
    imos.append(imos[i] + A[i])
mi = min(imos)
imos = [i - mi for i in imos]
N += 1

# 座標圧縮BIT
# alter: A[i] → alt_A[i]
# rev: alt[i] → A[i]
def compress(array):
    s = set(array)
    s = sorted(list(s))
    alter = {}
    rev = {}
    for i in range(len(s)):
        alter[s[i]] = i
        rev[i] = s[i]
    return alter, rev

alter, rev = compress(imos)
limit = N + 1
bit = BIT(limit)
ans = 0
for i in range(N):
    # 自身以下の数字が左にいくつあるか
    ans += bit.get(alter[imos[i]] + 2)
    bit.add(alter[imos[i]] + 1, 1)

print(ans)